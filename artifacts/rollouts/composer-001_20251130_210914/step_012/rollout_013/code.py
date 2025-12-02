
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),   # Ab
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=4.125, end=4.5),   # Eb
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.875),   # Ab
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),   # F7: F, A, C, Eb
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Sax: Motif - start it, leave it hanging, come back and finish it
# F6 (F), G#6 (Ab), C#6 (Db), F6 (F)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=84, start=1.5, end=1.875),   # F6
    pretty_midi.Note(velocity=110, pitch=86, start=1.875, end=2.25),  # G#6 (Ab)
    pretty_midi.Note(velocity=110, pitch=81, start=2.25, end=2.625),  # C#6 (Db)
    pretty_midi.Note(velocity=110, pitch=84, start=2.625, end=3.0),   # F6
    pretty_midi.Note(velocity=110, pitch=84, start=3.5, end=3.875),   # F6 again (reprise)
]
sax.notes.extend(sax_notes)

# Drums in bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),   # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),   # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),   # Snare on 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),   # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5625),# Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.3125),# Snare on 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0625),# Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=5.8125),# Snare on 4
]
# Hi-hat on every eighth
for i in range(1.5, 6.0, 0.1875):
    start = i
    end = start + 0.1875
    if end > 6.0:
        break
    pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
