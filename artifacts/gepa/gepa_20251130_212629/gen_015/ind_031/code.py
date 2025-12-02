
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the key: F major
key = 'F'

# Define time signature: 4/4
time_signature = (4, 4)

# Define instrument tracks
sax_track = pretty_midi.Instrument(program=64)  # Tenor sax
bass_track = pretty_midi.Instrument(program=33)  # Double bass
piano_track = pretty_midi.Instrument(program=0)  # Acoustic piano
drum_track = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

pm.instruments = [sax_track, bass_track, piano_track, drum_track]

# Time per bar (in seconds): 1.5s
bar_length = 1.5
# Time per beat (in seconds): 0.375s
beat_length = 0.375
# Time per eighth note: 0.1875s

# Function to create a note
def note(note_number, start, duration):
    return pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)

# ===================
# BAR 1: Little Ray (drums) plays alone
# ===================

# Kick on 1 and 3
drum_track.notes.append(note(36, 0.0, 0.1875))  # Kick on 1
drum_track.notes.append(note(36, 0.75, 0.1875))  # Kick on 3

# Snare on 2 and 4
drum_track.notes.append(note(38, 0.375, 0.1875))  # Snare on 2
drum_track.notes.append(note(38, 1.125, 0.1875))  # Snare on 4

# Hi-hat on every eighth
for i in range(8):
    drum_track.notes.append(note(42, i * 0.1875, 0.1875))

# ===================
# BAR 2: Everyone comes in
# ===================

# Bass line: F -> G -> Ab -> A (chromatic movement)
bass_notes = [71, 72, 73, 74]  # F, G, Ab, A
for i, note_num in enumerate(bass_notes):
    start_time = bar_length + i * beat_length
    duration = beat_length
    bass_track.notes.append(note(note_num, start_time, duration))

# Piano: 7th chords on beat 2 and 4 (F7 on 2, Bb7 on 4)
# F7 = F A C Eb
# Bb7 = Bb D F Ab
piano_notes = [
    # Beat 2 (F7)
    note(65, bar_length + 0.375, 0.1875),  # F
    note(69, bar_length + 0.375, 0.1875),  # A
    note(68, bar_length + 0.375, 0.1875),  # C
    note(67, bar_length + 0.375, 0.1875),  # Eb
    # Beat 4 (Bb7)
    note(62, bar_length + 1.125, 0.1875),  # Bb
    note(66, bar_length + 1.125, 0.1875),  # D
    note(65, bar_length + 1.125, 0.1875),  # F
    note(64, bar_length + 1.125, 0.1875),  # Ab
]

piano_track.notes.extend(piano_notes)

# Sax: Start the motif (F, G, Ab, rest)
sax_notes = [
    note(65, bar_length, 0.375),  # F
    note(67, bar_length + 0.375, 0.375),  # G
    note(68, bar_length + 0.75, 0.375),  # Ab
    # Rest
]

sax_track.notes.extend(sax_notes)

# ===================
# BAR 3: Continue with the motif, with space
# ===================

# Sax: repeats the motif, but with a slight variation in rhythm
sax_notes = [
    note(65, bar_length * 2, 0.1875),  # F
    note(67, bar_length * 2 + 0.1875, 0.375),  # G
    note(68, bar_length * 2 + 0.5625, 0.1875),  # Ab
    # Rest
]

sax_track.notes.extend(sax_notes)

# Bass: F -> G -> Ab -> Bb (chromatic movement)
bass_notes = [71, 72, 73, 75]
for i, note_num in enumerate(bass_notes):
    start_time = bar_length * 2 + i * beat_length
    duration = beat_length
    bass_track.notes.append(note(note_num, start_time, duration))

# Piano: 7th chords on beat 2 and 4 (F7 on 2, C7 on 4)
piano_notes = [
    # Beat 2 (F7)
    note(65, bar_length * 2 + 0.375, 0.1875),  # F
    note(69, bar_length * 2 + 0.375, 0.1875),  # A
    note(68, bar_length * 2 + 0.375, 0.1875),  # C
    note(67, bar_length * 2 + 0.375, 0.1875),  # Eb
    # Beat 4 (C7)
    note(67, bar_length * 2 + 1.125, 0.1875),  # C
    note(71, bar_length * 2 + 1.125, 0.1875),  # E
    note(68, bar_length * 2 + 1.125, 0.1875),  # G
    note(67, bar_length * 2 + 1.125, 0.1875),  # Bb
]

piano_track.notes.extend(piano_notes)

# Drums: Full bar
for i in range(8):
    drum_track.notes.append(note(42, bar_length * 2 + i * 0.1875, 0.1875))
drum_track.notes.append(note(36, bar_length * 2, 0.1875))  # Kick on 1
drum_track.notes.append(note(36, bar_length * 2 + 0.75, 0.1875))  # Kick on 3
drum_track.notes.append(note(38, bar_length * 2 + 0.375, 0.1875))  # Snare on 2
drum_track.notes.append(note(38, bar_length * 2 + 1.125, 0.1875))  # Snare on 4

# ===================
# BAR 4: Sax completes the motif
# ===================

# Sax: Return to the opening motif, completed
sax_notes = [
    note(65, bar_length * 3, 0.375),  # F
    note(67, bar_length * 3 + 0.375, 0.375),  # G
    note(68, bar_length * 3 + 0.75, 0.375),  # Ab
    # Rest
]

sax_track.notes.extend(sax_notes)

# Bass: F -> G -> Ab -> A (chromatic movement)
bass_notes = [71, 72, 73, 74]
for i, note_num in enumerate(bass_notes):
    start_time = bar_length * 3 + i * beat_length
    duration = beat_length
    bass_track.notes.append(note(note_num, start_time, duration))

# Piano: 7th chords on beat 2 and 4 (F7 on 2, Eb7 on 4)
piano_notes = [
    # Beat 2 (F7)
    note(65, bar_length * 3 + 0.375, 0.1875),  # F
    note(69, bar_length * 3 + 0.375, 0.1875),  # A
    note(68, bar_length * 3 + 0.375, 0.1875),  # C
    note(67, bar_length * 3 + 0.375, 0.1875),  # Eb
    # Beat 4 (Eb7)
    note(67, bar_length * 3 + 1.125, 0.1875),  # Eb
    note(71, bar_length * 3 + 1.125, 0.1875),  # G
    note(68, bar_length * 3 + 1.125, 0.1875),  # Bb
    note(67, bar_length * 3 + 1.125, 0.1875),  # D
]

piano_track.notes.extend(piano_notes)

# Drums: Full bar
for i in range(8):
    drum_track.notes.append(note(42, bar_length * 3 + i * 0.1875, 0.1875))
drum_track.notes.append(note(36, bar_length * 3, 0.1875))  # Kick on 1
drum_track.notes.append(note(36, bar_length * 3 + 0.75, 0.1875))  # Kick on 3
drum_track.notes.append(note(38, bar_length * 3 + 0.375, 0.1875))  # Snare on 2
drum_track.notes.append(note(38, bar_length * 3 + 1.125, 0.1875))  # Snare on 4

# Write the MIDI file
pm.write("dante_russo_intro.mid")
print("MIDI file written to 'dante_russo_intro.mid'")
