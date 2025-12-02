
import pretty_midi

# Create the MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42

# Bar 1 (0.0 - 1.5s): Little Ray alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Add some syncopation and dynamic velocity to make it feel alive

bar_duration = 1.5  # 4/4 time at 160 BPM = 1.5 seconds per bar
beats_per_bar = 4
beat_duration = bar_duration / beats_per_bar

# Drums: Bar 1
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    
    # Snare on 2 and 4
    pretty_midi.Note(velocity=85, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=95, pitch=38, start=1.5, end=1.625),
    
    # Hihat on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=60, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=60, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2-4 (1.5 - 6.0s): Full quartet
# Key: F minor
# Fm = F, Ab, C, Eb

# Bass: Walking line in Fm
# Chromatic approaches, no repetition

# Bass notes: F, Gb, G, A, Bb, B, C, Db, D, Eb, F
# Walking line in Fm: F, Gb, Ab, A, Bb, B, C, Db, D, Eb, F

bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.625),   # F
    pretty_midi.Note(velocity=80, pitch=64, start=1.625, end=1.75),   # Gb
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=1.875),   # Ab
    pretty_midi.Note(velocity=80, pitch=68, start=1.875, end=2.0),    # A
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.125),    # Bb
    pretty_midi.Note(velocity=80, pitch=70, start=2.125, end=2.25),   # B
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.375),   # C
    pretty_midi.Note(velocity=80, pitch=72, start=2.375, end=2.5),    # Db
    pretty_midi.Note(velocity=80, pitch=73, start=2.5, end=2.625),    # D
    pretty_midi.Note(velocity=80, pitch=74, start=2.625, end=2.75),   # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=2.75, end=2.875),   # F
    pretty_midi.Note(velocity=80, pitch=64, start=2.875, end=3.0),    # Gb
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.125),    # Ab
    pretty_midi.Note(velocity=80, pitch=68, start=3.125, end=3.25),   # A
    pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.375),   # Bb
    pretty_midi.Note(velocity=80, pitch=70, start=3.375, end=3.5),    # B
    pretty_midi.Note(velocity=80, pitch=71, start=3.5, end=3.625),    # C
    pretty_midi.Note(velocity=80, pitch=72, start=3.625, end=3.75),   # Db
    pretty_midi.Note(velocity=80, pitch=73, start=3.75, end=3.875),   # D
    pretty_midi.Note(velocity=80, pitch=74, start=3.875, end=4.0),    # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=4.0, end=4.125),    # F
    pretty_midi.Note(velocity=80, pitch=64, start=4.125, end=4.25),   # Gb
    pretty_midi.Note(velocity=80, pitch=67, start=4.25, end=4.375),   # Ab
    pretty_midi.Note(velocity=80, pitch=68, start=4.375, end=4.5),    # A
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.625),    # Bb
    pretty_midi.Note(velocity=80, pitch=70, start=4.625, end=4.75),   # B
    pretty_midi.Note(velocity=80, pitch=71, start=4.75, end=4.875),   # C
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.0),    # Db
    pretty_midi.Note(velocity=80, pitch=73, start=5.0, end=5.125),    # D
    pretty_midi.Note(velocity=80, pitch=74, start=5.125, end=5.25),   # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.375),   # F
    pretty_midi.Note(velocity=80, pitch=64, start=5.375, end=5.5),    # Gb
    pretty_midi.Note(velocity=80, pitch=67, start=5.5, end=5.625),    # Ab
    pretty_midi.Note(velocity=80, pitch=68, start=5.625, end=5.75),   # A
    pretty_midi.Note(velocity=80, pitch=69, start=5.75, end=5.875),   # Bb
    pretty_midi.Note(velocity=80, pitch=70, start=5.875, end=6.0),    # B
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
# Bb7 = Bb, D, F, Ab
# Eb7 = Eb, G, Bb, Db
# Ab7 = Ab, C, Eb, G

# Comp on 2 and 4
# Bar 2: Fm7 on 2, Bb7 on 4
# Bar 3: Eb7 on 2, Ab7 on 4
# Bar 4: Fm7 on 2, Bb7 on 4

# Bar 2: Fm7 on 2 (1.875 - 2.0), Bb7 on 4 (2.5 - 2.625)
# Bar 3: Eb7 on 2 (3.125 - 3.25), Ab7 on 4 (3.75 - 3.875)
# Bar 4: Fm7 on 2 (4.375 - 4.5), Bb7 on 4 (4.875 - 5.0)

# Fm7
f7_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.0),
]
for note in f7_notes:
    piano.notes.append(note)

# Bb7
bb7_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.625),
    pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=2.625),
    pretty_midi.Note(velocity=90, pitch=65, start=2.5, end=2.625),
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.625),
]
for note in bb7_notes:
    piano.notes.append(note)

# Eb7
eb7_notes = [
    pretty_midi.Note(velocity=90, pitch=74, start=3.125, end=3.25),
    pretty_midi.Note(velocity=90, pitch=77, start=3.125, end=3.25),
    pretty_midi.Note(velocity=90, pitch=69, start=3.125, end=3.25),
    pretty_midi.Note(velocity=90, pitch=72, start=3.125, end=3.25),
]
for note in eb7_notes:
    piano.notes.append(note)

# Ab7
ab7_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=77, start=3.75, end=3.875),
]
for note in ab7_notes:
    piano.notes.append(note)

# Fm7 again
for note in f7_notes:
    piano.notes.append(note)

# Bb7 again
for note in bb7_notes:
    piano.notes.append(note)

# Saxophone melody: Fm, simple yet haunting

# Melody: F, Ab, G, Eb (melodic minor)
# Play on the first beat of bar 2, leave it hanging, then come back in bar 4

# Bar 2
sax_note1 = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875)
sax_note2 = pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25)
sax_note3 = pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625)
sax_note4 = pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0)

# Bar 4
sax_note5 = pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875)
sax_note6 = pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25)
sax_note7 = pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.625)
sax_note8 = pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0)

# Add the notes to the sax instrument
for note in [sax_note1, sax_note2, sax_note3, sax_note4, sax_note5, sax_note6, sax_note7, sax_note8]:
    sax.notes.append(note)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
