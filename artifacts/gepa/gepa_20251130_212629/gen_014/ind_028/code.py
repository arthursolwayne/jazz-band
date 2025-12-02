
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick=36, snare=38, hihat=42, ride=48
# Bar 1 (0.0 - 1.5s): Little Ray on drums only
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    
    # Snare on 2 and 4
    pretty_midi.Note(velocity=95, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=95, pitch=38, start=1.875, end=2.25),
    
    # Hi-hat on every eighth note
    pretty_midi.Note(velocity=85, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=85, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=85, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=85, pitch=42, start=1.125, end=1.5)
]

# Add the drum notes
for note in drum_notes:
    drums.notes.append(note)

# Bar 2 (1.5 - 3.0s): Full quartet
# Bass line: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875),  # Dm7 root
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.25),  # Eb (chromatic)
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=2.625, end=3.0)   # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # D
    
    # Dm7 on beat 4
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75)   # D
]
piano.notes.extend(piano_notes)

# Saxophone: Simple motif, haunting and concise
# Motif: D (62) - F (65) - Bb (69) - D (72)
# Start on beat 2 (1.875s), end on beat 3 (2.625s), leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=69, start=2.125, end=2.25),
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.375)
]
sax.notes.extend(sax_notes)

# Bar 3 (3.0 - 4.5s): Full quartet
# Bass continues walking
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5)   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # D
    
    # Dm7 on beat 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25)   # D
]
piano.notes.extend(piano_notes)

# Sax motif repeat, slightly altered — leave it hanging again
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.875, end=4.0),
    pretty_midi.Note(velocity=110, pitch=65, start=4.0, end=4.125),
    pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.25),
    pretty_midi.Note(velocity=110, pitch=72, start=4.25, end=4.375)
]
sax.notes.extend(sax_notes)

# Bar 4 (4.5 - 6.0s): Full quartet
# Bass continues the walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0)   # F
]
bass.notes.extend(bass_notes)

# Piano: Final comp
piano_notes = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),  # D
    
    # Dm7 on beat 4
    pretty_midi.Note(velocity=100, pitch=62, start=6.0, end=6.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=6.0, end=6.375),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=6.0, end=6.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=6.0, end=6.375)   # D
]
piano.notes.extend(piano_notes)

# Final sax note — D, left to hang
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=5.625, end=5.75)
]
sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("wayne_intro.mid")
