
import pretty_midi

# Initialize the MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1 (beat 0-1.5s)
drum_notes = [
    # Kick on beat 0, 0.75s (beat 1), 1.5s (beat 2), 2.25s (beat 3)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    
    # Snare on beat 0.375s (beat 1), 1.125s (beat 2), 1.875s (beat 3), 2.625s (beat 4)
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    
    # Hihat on every eighth note
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4 (1.5s to 6.0s)
# Bar 2: 1.5 - 3.0s
# Bar 3: 3.0 - 4.5s
# Bar 4: 4.5 - 6.0s

# Bass: Walking line, chromatic approaches, no repeated notes
# F minor key (F, Gb, Ab, Bb, C, Db, Eb) — but we’ll use F minor pentatonic for simplicity

# Bass line:
# Bar 2: F -> Gb -> Ab -> A
# Bar 3: Bb -> C -> Db -> Eb
# Bar 4: F -> Gb -> Ab -> A (return to F)

bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=2.0, end=2.5),  # Gb
    pretty_midi.Note(velocity=80, pitch=68, start=2.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.5),  # A

    pretty_midi.Note(velocity=80, pitch=67, start=3.5, end=4.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=4.0, end=4.5),  # C
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=5.0),  # Db
    pretty_midi.Note(velocity=80, pitch=65, start=5.0, end=5.5),  # Eb

    pretty_midi.Note(velocity=80, pitch=71, start=5.5, end=6.0),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=5.5, end=6.0),  # Gb
    pretty_midi.Note(velocity=80, pitch=68, start=5.5, end=6.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=5.5, end=6.0)   # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (Bar 2: 2.0s, 3.0s; Bar 3: 4.0s, 5.0s; Bar 4: 6.0s, 7.0s)
# F7 = F, A, C, Eb
# Ab7 = Ab, C, Eb, Gb
# Bb7 = Bb, D, F, Ab

# Bar 2 (2.0s & 3.0s)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=2.0, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=74, start=2.0, end=2.5),  # A
    pretty_midi.Note(velocity=80, pitch=76, start=2.0, end=2.5),  # C
    pretty_midi.Note(velocity=80, pitch=73, start=2.0, end=2.5),  # Eb

    pretty_midi.Note(velocity=80, pitch=68, start=3.0, end=3.5),  # Ab
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.5),  # C
    pretty_midi.Note(velocity=80, pitch=73, start=3.0, end=3.5),  # Eb
    pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.5),  # Gb
]

# Bar 3 (4.0s & 5.0s)
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=67, start=4.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=4.0, end=4.5),  # D
    pretty_midi.Note(velocity=80, pitch=71, start=4.0, end=4.5),  # F
    pretty_midi.Note(velocity=80, pitch=68, start=4.0, end=4.5),  # Ab
])

# Bar 4 (6.0s)
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=71, start=6.0, end=6.5),  # F
    pretty_midi.Note(velocity=80, pitch=74, start=6.0, end=6.5),  # A
    pretty_midi.Note(velocity=80, pitch=76, start=6.0, end=6.5),  # C
    pretty_midi.Note(velocity=80, pitch=73, start=6.0, end=6.5),  # Eb
])

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif in F minor – simple, melodic, emotional.
# Melody: F -> Ab -> Bb -> C (Bars 2-4)
# Each note is a quarter note, played over 6 seconds (160 BPM = 0.375s per beat)

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=2.0, end=2.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5),  # C

    pretty_midi.Note(velocity=100, pitch=68, start=3.5, end=4.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.5),  # F

    pretty_midi.Note(velocity=100, pitch=68, start=5.5, end=6.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=6.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=6.0)   # F
]

for note in sax_notes:
    sax.notes.append(note)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_4_bar_intro.mid")
