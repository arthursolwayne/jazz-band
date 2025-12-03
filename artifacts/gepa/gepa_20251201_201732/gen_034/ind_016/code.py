
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),  # F2 (chromatic approach)

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.75), # A2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=47, start=3.75, end=4.125), # B2
    pretty_midi.Note(velocity=90, pitch=46, start=4.125, end=4.5),  # Bb2 (chromatic approach)

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=4.875),  # B2
    pretty_midi.Note(velocity=90, pitch=49, start=4.875, end=5.25), # C3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.625), # C#3
    pretty_midi.Note(velocity=90, pitch=48, start=5.625, end=6.0),  # B2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # C#4

    # Bar 3: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C4

    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([
        pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
        pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375),
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75),
        pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75),
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5),
        pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    ])

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F#4 - Bb4 (suspended), then resolve to C4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75),  # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=1.875),  # Bb4 (suspension)
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.375),  # C4 (resolve)
    pretty_midi.Note(velocity=110, pitch=62, start=2.375, end=2.5),   # D4
    pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=2.625),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=2.75), # A4
    pretty_midi.Note(velocity=110, pitch=62, start=2.75, end=2.875), # D4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_introduction.mid')
