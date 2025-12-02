
import pretty_midi

# Initialize the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature (4/4)
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Create an instrument group
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # MIDI percussion uses piano program
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

piano = pretty_midi.Instrument(program=piano_program)
bass = pretty_midi.Instrument(program=bass_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to the MIDI file
midi.instruments = [piano, bass, drums, sax]

# Define note durations in seconds
beat = 0.375  # 160 BPM => 60 / 160 = 0.375 seconds per beat
quarter = beat
eighth = beat / 2
sixteenth = beat / 4

# --- BAR 1: Little Ray on drums --- (4 beats)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on 1 and 3 (beats 0 and 2)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.0 + sixteenth))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.0 + sixteenth))

# Snare on 2 and 4 (beats 1 and 3)
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.0, end=1.0 + sixteenth))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.0 + sixteenth))

# Hihat on every eighth
for i in range(8):
    start = i * eighth
    end = start + sixteenth
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# --- BAR 2: Everyone in, sax melody (Dm7 voicing) ---
# Dm7 = D, F, A, C (root, flat 3, 5, flat 7)
# Key: Dm (D, F, A, C)

# Bass: Walking line, chromatic approach to D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=4.0, end=4.0 + quarter))  # C (chromatic approach to D)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=4.0 + quarter, end=4.0 + quarter * 2))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=4.0 + quarter * 2, end=4.0 + quarter * 3))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=4.0 + quarter * 3, end=4.0 + quarter * 4))  # D

# Piano: Comp on 2 and 4 with 7th chords
# Bar 2: Dm7
piano.notes.append(pretty_midi.Note(velocity=85, pitch=62, start=4.0, end=4.0 + quarter))  # D
piano.notes.append(pretty_midi.Note(velocity=85, pitch=64, start=4.0, end=4.0 + quarter))  # F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=67, start=4.0, end=4.0 + quarter))  # A
piano.notes.append(pretty_midi.Note(velocity=85, pitch=69, start=4.0, end=4.0 + quarter))  # C

# Bar 3: G7 (chromatic approach to C)
piano.notes.append(pretty_midi.Note(velocity=85, pitch=67, start=6.0, end=6.0 + quarter))  # G
piano.notes.append(pretty_midi.Note(velocity=85, pitch=69, start=6.0, end=6.0 + quarter))  # B
piano.notes.append(pretty_midi.Note(velocity=85, pitch=71, start=6.0, end=6.0 + quarter))  # D
piano.notes.append(pretty_midi.Note(velocity=85, pitch=69, start=6.0, end=6.0 + quarter))  # Bb

# Bar 4: Cmaj7 (resolution)
piano.notes.append(pretty_midi.Note(velocity=85, pitch=72, start=8.0, end=8.0 + quarter))  # C
piano.notes.append(pretty_midi.Note(velocity=85, pitch=74, start=8.0, end=8.0 + quarter))  # E
piano.notes.append(pretty_midi.Note(velocity=85, pitch=76, start=8.0, end=8.0 + quarter))  # G
piano.notes.append(pretty_midi.Note(velocity=85, pitch=79, start=8.0, end=8.0 + quarter))  # B

# --- Sax: Melody in Dm (4 bars, 1 motif, leave it hanging) ---
# Melody: D - F - Eb - D (hanging on D)
# Start on beat 4.0

sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.0 + eighth))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.0 + eighth, end=4.0 + quarter))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.0 + quarter, end=4.0 + quarter + eighth))  # Eb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.0 + quarter + eighth, end=4.0 + quarter * 2))  # D (hanging)

# Save the MIDI file
midi.write('dante_russo_intro.mid')

print("MIDI file saved as 'dante_russo_intro.mid'")
