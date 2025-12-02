
import pretty_midi

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time per bar in seconds
bar_length = 1.5
beat_length = bar_length / 4

# Create instruments
drums = pretty_midi.Instrument(program=10)  # Drums
bass = pretty_midi.Instrument(program=33)    # Acoustic Bass
piano = pretty_midi.Instrument(program=0)   # Acoustic Piano
sax = pretty_midi.Instrument(program=64)    # Tenor Saxophone

pm.instruments = [drums, bass, piano, sax]

# Function to add a note to an instrument
def add_note(instrument, pitch, start, end, velocity=100):
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=end)
    instrument.notes.append(note)

# ---- BAR 1: Drums only (Urgent, driving)
# Kick on beat 1 and 3
add_note(drums, 36, 0, beat_length)  # Kick on beat 1
add_note(drums, 36, 2 * beat_length, 3 * beat_length)  # Kick on beat 3

# Snare on beat 2 and 4
add_note(drums, 38, 1 * beat_length, 1.5 * beat_length)  # Snare on beat 2
add_note(drums, 38, 3 * beat_length, 3.5 * beat_length)  # Snare on beat 4

# Hi-hat on every eighth note
for t in [0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625, 3, 3.375, 3.75, 4.125]:
    add_note(drums, 42, t, t + 0.375)

# ---- BAR 2: Full ensemble
# Saxophone motif: F4 -> G4 -> A4 -> Bb4 (but leave it hanging)
add_note(sax, 66, 3, 3.25)  # F4
add_note(sax, 67, 3.25, 3.5)  # G4
add_note(sax, 69, 3.5, 3.75)  # A4
add_note(sax, 70, 3.75, 4)    # Bb4

# Bass: F4 -> G4 -> A4 -> Bb4 (walking line with chromatic approach)
add_note(bass, 66, 3, 3.25)
add_note(bass, 67, 3.25, 3.5)
add_note(bass, 69, 3.5, 3.75)
add_note(bass, 70, 3.75, 4)

# Piano: F7 chord on beat 2 and 4 (F, A, C, E)
# Beat 2
add_note(piano, 66, 3.5, 3.75)  # F4
add_note(piano, 69, 3.5, 3.75)  # A4
add_note(piano, 72, 3.5, 3.75)  # C5
add_note(piano, 76, 3.5, 3.75)  # E5

# Beat 4
add_note(piano, 66, 3.75, 4)
add_note(piano, 69, 3.75, 4)
add_note(piano, 72, 3.75, 4)
add_note(piano, 76, 3.75, 4)

# ---- BAR 3: A return to the motif
# Saxophone motif: F4 -> G4 -> A4 -> F4 (resolve back to F)
add_note(sax, 66, 4.5, 4.75)
add_note(sax, 67, 4.75, 5)
add_note(sax, 69, 5, 5.25)
add_note(sax, 66, 5.25, 5.5)

# Bass: G4 -> A4 -> Bb4 -> C5
add_note(bass, 67, 4.5, 4.75)
add_note(bass, 69, 4.75, 5)
add_note(bass, 70, 5, 5.25)
add_note(bass, 72, 5.25, 5.5)

# Piano: F7 chord on beat 2 and 4
# Beat 2
add_note(piano, 66, 5.5, 5.75)
add_note(piano, 69, 5.5, 5.75)
add_note(piano, 72, 5.5, 5.75)
add_note(piano, 76, 5.5, 5.75)

# Beat 4
add_note(piano, 66, 5.75, 6)
add_note(piano, 69, 5.75, 6)
add_note(piano, 72, 5.75, 6)
add_note(piano, 76, 5.75, 6)

# ---- BAR 4: Full resolution
# Saxophone motif: F4 -> G4 -> A4 -> F4 (full resolution)
add_note(sax, 66, 6, 6.25)
add_note(sax, 67, 6.25, 6.5)
add_note(sax, 69, 6.5, 6.75)
add_note(sax, 66, 6.75, 7)

# Bass: A4 -> Bb4 -> C5 -> D5 (walking line)
add_note(bass, 69, 6, 6.25)
add_note(bass, 70, 6.25, 6.5)
add_note(bass, 72, 6.5, 6.75)
add_note(bass, 74, 6.75, 7)

# Piano: F7 chord on beat 2 and 4
# Beat 2
add_note(piano, 66, 6.5, 6.75)
add_note(piano, 69, 6.5, 6.75)
add_note(piano, 72, 6.5, 6.75)
add_note(piano, 76, 6.5, 6.75)

# Beat 4
add_note(piano, 66, 6.75, 7)
add_note(piano, 69, 6.75, 7)
add_note(piano, 72, 6.75, 7)
add_note(piano, 76, 6.75, 7)

# ---- Save the MIDI file
pm.write("wayne_intro.mid")
