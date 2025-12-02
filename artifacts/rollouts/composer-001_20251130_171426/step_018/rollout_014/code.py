
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
    # Hi-hat on every eighth note
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4
# Bar 2 (1.5 - 3.0s)
# Sax: short motif starting at 1.5s - D (D4), E (E4), F# (F#4), D (D4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=66, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),
]
sax.notes.extend(sax_notes)

# Bass: walking line in D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=1.5, end=1.75),  # D3
    pretty_midi.Note(velocity=80, pitch=47, start=1.75, end=2.0),  # Eb3
    pretty_midi.Note(velocity=80, pitch=49, start=2.0, end=2.25),  # F#3
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.5),  # G3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # D7 on 2 (1.75 - 2.0)
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # B4
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # E4
    # G7 on 4 (2.5 - 2.75)
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.75),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=2.75),  # D5
    pretty_midi.Note(velocity=90, pitch=74, start=2.5, end=2.75),  # E5
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),  # B4
]
piano.notes.extend(piano_notes)

# Bar 3 (3.0 - 4.5s)
# Sax: repeat the motif but transposed up a third
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),
]
sax.notes.extend(sax_notes)

# Bass: walking line in D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.25),  # G3
    pretty_midi.Note(velocity=80, pitch=51, start=3.25, end=3.5),  # Ab3
    pretty_midi.Note(velocity=80, pitch=53, start=3.5, end=3.75),  # B3
    pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=4.0),  # C4
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # G7 on 2 (3.25 - 3.5)
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=3.25, end=3.5),  # D5
    pretty_midi.Note(velocity=90, pitch=74, start=3.25, end=3.5),  # E5
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),  # B4
    # B7 on 4 (4.0 - 4.25)
    pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.25),  # B4
    pretty_midi.Note(velocity=90, pitch=76, start=4.0, end=4.25),  # F#5
    pretty_midi.Note(velocity=90, pitch=78, start=4.0, end=4.25),  # G5
    pretty_midi.Note(velocity=90, pitch=73, start=4.0, end=4.25),  # D5
]
piano.notes.extend(piano_notes)

# Bar 4 (4.5 - 6.0s)
# Sax: complete the motif, resolve to D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=66, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),
]
sax.notes.extend(sax_notes)

# Bass: walking line in D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=55, start=4.5, end=4.75),  # C4
    pretty_midi.Note(velocity=80, pitch=56, start=4.75, end=5.0),  # Db4
    pretty_midi.Note(velocity=80, pitch=58, start=5.0, end=5.25),  # D4
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.5),  # E4
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # D7 on 2 (4.75 - 5.0)
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),  # B4
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),  # E4
    # F#7 on 4 (5.5 - 5.75)
    pretty_midi.Note(velocity=90, pitch=66, start=5.5, end=5.75),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=5.5, end=5.75),  # C#5
    pretty_midi.Note(velocity=90, pitch=73, start=5.5, end=5.75),  # D5
    pretty_midi.Note(velocity=90, pitch=68, start=5.5, end=5.75),  # G4
]
piano.notes.extend(piano_notes)

# Add more drums for bars 2-4
# Bar 2 (1.5 - 3.0s)
for i in range(2):
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=1.5 + i*1.5, end=1.5 + i*1.5 + 0.375),
        pretty_midi.Note(velocity=110, pitch=38, start=1.5 + i*1.5 + 0.75, end=1.5 + i*1.5 + 0.875),
        pretty_midi.Note(velocity=90, pitch=42, start=1.5 + i*1.5, end=1.5 + i*1.5 + 0.375),
        pretty_midi.Note(velocity=90, pitch=42, start=1.5 + i*1.5 + 0.375, end=1.5 + i*1.5 + 0.75),
        pretty_midi.Note(velocity=90, pitch=42, start=1.5 + i*1.5 + 0.75, end=1.5 + i*1.5 + 1.125),
        pretty_midi.Note(velocity=90, pitch=42, start=1.5 + i*1.5 + 1.125, end=1.5 + i*1.5 + 1.5),
    ]
    drums.notes.extend(drum_notes)

# Bar 3 (3.0 - 4.5s)
for i in range(2):
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=3.0 + i*1.5, end=3.0 + i*1.5 + 0.375),
        pretty_midi.Note(velocity=110, pitch=38, start=3.0 + i*1.5 + 0.75, end=3.0 + i*1.5 + 0.875),
        pretty_midi.Note(velocity=90, pitch=42, start=3.0 + i*1.5, end=3.0 + i*1.5 + 0.375),
        pretty_midi.Note(velocity=90, pitch=42, start=3.0 + i*1.5 + 0.375, end=3.0 + i*1.5 + 0.75),
        pretty_midi.Note(velocity=90, pitch=42, start=3.0 + i*1.5 + 0.75, end=3.0 + i*1.5 + 1.125),
        pretty_midi.Note(velocity=90, pitch=42, start=3.0 + i*1.5 + 1.125, end=3.0 + i*1.5 + 1.5),
    ]
    drums.notes.extend(drum_notes)

# Bar 4 (4.5 - 6.0s)
for i in range(2):
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=4.5 + i*1.5, end=4.5 + i*1.5 + 0.375),
        pretty_midi.Note(velocity=110, pitch=38, start=4.5 + i*1.5 + 0.75, end=4.5 + i*1.5 + 0.875),
        pretty_midi.Note(velocity=90, pitch=42, start=4.5 + i*1.5, end=4.5 + i*1.5 + 0.375),
        pretty_midi.Note(velocity=90, pitch=42, start=4.5 + i*1.5 + 0.375, end=4.5 + i*1.5 + 0.75),
        pretty_midi.Note(velocity=90, pitch=42, start=4.5 + i*1.5 + 0.75, end=4.5 + i*1.5 + 1.125),
        pretty_midi.Note(velocity=90, pitch=42, start=4.5 + i*1.5 + 1.125, end=4.5 + i*1.5 + 1.5),
    ]
    drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
