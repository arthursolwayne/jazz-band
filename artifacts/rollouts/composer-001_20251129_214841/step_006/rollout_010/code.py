
import pretty_midi

midi = pretty_midi.PrettyMIDI(tempo=120 * 1000 / 60)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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

# Bar 2: Full ensemble (1.5 - 3.0s)
# Sax: start motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # C
]
sax.notes.extend(sax_notes)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=49, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=1.75, end=2.0),  # Db
    pretty_midi.Note(velocity=90, pitch=51, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=2.25, end=2.5),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # C7 on 2 (1.75 - 2.0)
    pretty_midi.Note(velocity=95, pitch=60, start=1.75, end=2.0),
    pretty_midi.Note(velocity=95, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=95, pitch=67, start=1.75, end=2.0),
    # F7 on 4 (2.5 - 2.75)
    pretty_midi.Note(velocity=95, pitch=65, start=2.5, end=2.75),
    pretty_midi.Note(velocity=95, pitch=69, start=2.5, end=2.75),
    pretty_midi.Note(velocity=95, pitch=72, start=2.5, end=2.75),
]
piano.notes.extend(piano_notes)

# Bar 3: Full ensemble (3.0 - 4.5s)
# Sax: repeat motif, lower by minor third
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=49, start=3.0, end=3.25),  # C (lowered 3rd)
    pretty_midi.Note(velocity=110, pitch=51, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=110, pitch=52, start=3.5, end=3.75),  # Eb
    pretty_midi.Note(velocity=110, pitch=49, start=3.75, end=4.0),  # C
]
sax.notes.extend(sax_notes)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=49, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=3.25, end=3.5),  # Db
    pretty_midi.Note(velocity=90, pitch=51, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=3.75, end=4.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # C7 on 2 (3.25 - 3.5)
    pretty_midi.Note(velocity=95, pitch=60, start=3.25, end=3.5),
    pretty_midi.Note(velocity=95, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=95, pitch=67, start=3.25, end=3.5),
    # F7 on 4 (4.0 - 4.25)
    pretty_midi.Note(velocity=95, pitch=65, start=4.0, end=4.25),
    pretty_midi.Note(velocity=95, pitch=69, start=4.0, end=4.25),
    pretty_midi.Note(velocity=95, pitch=72, start=4.0, end=4.25),
]
piano.notes.extend(piano_notes)

# Bar 4: Full ensemble (4.5 - 6.0s)
# Sax: finish motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),  # C
]
sax.notes.extend(sax_notes)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=49, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=4.75, end=5.0),  # Db
    pretty_midi.Note(velocity=90, pitch=51, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=5.25, end=5.5),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # C7 on 2 (4.75 - 5.0)
    pretty_midi.Note(velocity=95, pitch=60, start=4.75, end=5.0),
    pretty_midi.Note(velocity=95, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=95, pitch=67, start=4.75, end=5.0),
    # F7 on 4 (5.5 - 5.75)
    pretty_midi.Note(velocity=95, pitch=65, start=5.5, end=5.75),
    pretty_midi.Note(velocity=95, pitch=69, start=5.5, end=5.75),
    pretty_midi.Note(velocity=95, pitch=72, start=5.5, end=5.75),
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4
for bar in [3, 4]:
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.0, end=start + 0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.1875, end=start + 0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.5625, end=start + 0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.9375, end=start + 1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.3125, end=start + 1.5),
    drums.notes.extend([

])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
