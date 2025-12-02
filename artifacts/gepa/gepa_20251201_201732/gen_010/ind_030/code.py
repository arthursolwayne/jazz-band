
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root) -> F#2 (fifth) -> E2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    # Bar 3: A2 (root) -> C#3 (fifth) -> B2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=100, pitch=50, start=2.8125, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=49, start=3.1875, end=3.5625),
    # Bar 4: B2 (root) -> D3 (fifth) -> C#3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=49, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=54, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=53, start=4.125, end=4.5)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dmaj7 (D, F#, A, C#)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    # Bar 3: Am7 (A, C#, E, G)
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=100, pitch=77, start=2.625, end=2.8125),
    # Bar 4: Bm7 (B, D, F#, A)
    pretty_midi.Note(velocity=100, pitch=71, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=76, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=78, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=81, start=3.5625, end=3.75)
]
piano.notes.extend(piano_notes)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [1.5, 3.0, 4.5]:
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hihat
    for i in range(0, 4):
        start = bar_start + i * 0.375
        pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.1875)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.875),  # A4
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=72, start=2.625, end=2.8125),  # C#5
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=72, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125),  # A4 again
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5)    # F#4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
