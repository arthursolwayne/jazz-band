
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root) with chromatic approach on D#2
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=39, start=1.5, end=1.625),
    # Bar 3: A2 (fifth) with chromatic approach on G#2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.375),
    # Bar 4: D2 (root) with chromatic approach on D#2
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=39, start=3.0, end=3.125),
]
bass.notes.extend(bass_notes)

# Piano: open voicings, resolving on the last chord of each bar
piano_notes = [
    # Bar 2: Dmaj7 (D, F#, A, C#)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0),
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=2.0),
    pretty_midi.Note(velocity=85, pitch=71, start=1.5, end=2.0),
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=2.0),
    # Bar 3: Bm7 (B, D, F#, A)
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.5),
    pretty_midi.Note(velocity=80, pitch=67, start=2.0, end=2.5),
    pretty_midi.Note(velocity=85, pitch=69, start=2.0, end=2.5),
    pretty_midi.Note(velocity=80, pitch=72, start=2.0, end=2.5),
    # Bar 4: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=3.0),
    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=3.0),
    pretty_midi.Note(velocity=85, pitch=71, start=2.5, end=3.0),
    pretty_midi.Note(velocity=80, pitch=64, start=2.5, end=3.0),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [1.5, 3.0, 4.5]:
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hi-hat on every eighth
    for i in range(8):
        start = bar_start + i * 0.1875
        end = start + 0.1875
        pretty_midi.Note(velocity=80, pitch=42, start=start, end=end)
drums.notes.extend([note for note in drums.notes if note.start >= 1.5])

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif on D4 (62), E4 (64), F#4 (66)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=105, pitch=64, start=1.625, end=1.75),
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=1.875),
    # Bar 3: Leave it hanging on A4 (69)
    pretty_midi.Note(velocity=105, pitch=69, start=2.25, end=2.375),
    # Bar 4: Return and finish the motif
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125),
    pretty_midi.Note(velocity=105, pitch=64, start=3.125, end=3.25),
    pretty_midi.Note(velocity=110, pitch=66, start=3.25, end=3.375),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
