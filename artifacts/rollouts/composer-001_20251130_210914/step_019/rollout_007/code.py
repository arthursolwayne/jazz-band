
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass - walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=63, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=63, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Diane on piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=81, start=1.5, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=81, start=3.0, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=81, start=4.5, end=4.875),
]
for note in piano_notes:
    piano.notes.append(note)

# Dante on sax - one short motif, make it sing
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Bar 2
for i in range(4):
    kick = pretty_midi.Note(velocity=100, pitch=36, start=1.5 + i*0.75, end=1.5 + i*0.75 + 0.375)
    snare = pretty_midi.Note(velocity=110, pitch=38, start=1.5 + i*0.75 + 0.375, end=1.5 + i*0.75 + 0.75)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=1.5 + i*0.75, end=1.5 + i*0.75 + 0.375)
    hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=1.5 + i*0.75 + 0.375, end=1.5 + i*0.75 + 0.75)
    hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=1.5 + i*0.75 + 0.75, end=1.5 + i*0.75 + 1.125)
    drums.notes.append(kick)
    drums.notes.append(snare)
    drums.notes.append(hihat)
    drums.notes.append(hihat2)
    drums.notes.append(hihat3)

# Bar 3
for i in range(4):
    kick = pretty_midi.Note(velocity=100, pitch=36, start=3.0 + i*0.75, end=3.0 + i*0.75 + 0.375)
    snare = pretty_midi.Note(velocity=110, pitch=38, start=3.0 + i*0.75 + 0.375, end=3.0 + i*0.75 + 0.75)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=3.0 + i*0.75, end=3.0 + i*0.75 + 0.375)
    hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=3.0 + i*0.75 + 0.375, end=3.0 + i*0.75 + 0.75)
    hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=3.0 + i*0.75 + 0.75, end=3.0 + i*0.75 + 1.125)
    drums.notes.append(kick)
    drums.notes.append(snare)
    drums.notes.append(hihat)
    drums.notes.append(hihat2)
    drums.notes.append(hihat3)

# Bar 4
for i in range(4):
    kick = pretty_midi.Note(velocity=100, pitch=36, start=4.5 + i*0.75, end=4.5 + i*0.75 + 0.375)
    snare = pretty_midi.Note(velocity=110, pitch=38, start=4.5 + i*0.75 + 0.375, end=4.5 + i*0.75 + 0.75)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=4.5 + i*0.75, end=4.5 + i*0.75 + 0.375)
    hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=4.5 + i*0.75 + 0.375, end=4.5 + i*0.75 + 0.75)
    hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=4.5 + i*0.75 + 0.75, end=4.5 + i*0.75 + 1.125)
    drums.notes.append(kick)
    drums.notes.append(snare)
    drums.notes.append(hihat)
    drums.notes.append(hihat2)
    drums.notes.append(hihat3)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
