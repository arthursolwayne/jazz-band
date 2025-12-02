
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Set tempo and time signature
tempo = 160
time_signature = (4, 4)
duration = 6.0  # seconds for 4 bars at 160 BPM

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=tempo, time_signature=(4, 4))

# Define instruments
drums = Instrument(program=Program.DRUMS)
bass = Instrument(program=Program.ELECTRIC_BASS_FINGER)
piano = Instrument(program=Program.ELECTRIC_PIANO_1)
sax = Instrument(program=Program.TENOR_SAX)
pm.instruments = [drums, bass, piano, sax]

# Time per bar
time_per_bar = 60.0 / tempo * 4  # 60 seconds per minute, 4 beats per bar
time_per_beat = time_per_bar / 4  # 4 beats per bar
time_per_eighth = time_per_beat / 2

# ------------------
# DRUMS (Little Ray)
# ------------------
# Kick on 1 and 3
kick_notes = [Note(36, 100, 0, time_per_beat), Note(36, 100, 2 * time_per_beat)]
# Snare on 2 and 4
snare_notes = [Note(38, 100, 1 * time_per_beat), Note(38, 100, 3 * time_per_beat)]
# Hihat on every eighth
hihat_notes = [Note(42, 80, t * time_per_eighth) for t in range(8)]

drums.notes.extend(kick_notes)
drums.notes.extend(snare_notes)
drums.notes.extend(hihat_notes)

# ------------------
# BASS (Marcus)
# ------------------
# Walking line in Fm
# Fm scale: F, Gb, Ab, A, Bb, C, Db
# Walking bass: F -> Gb -> Ab -> A -> Bb -> C -> Db -> F...

# Times for each note (from 0 to 4 bars in eighth notes)
bass_notes = [
    Note(53, 80, 0, time_per_eighth),    # F
    Note(51, 80, time_per_eighth, time_per_eighth),  # Gb
    Note(49, 80, 2 * time_per_eighth, time_per_eighth),  # Ab
    Note(50, 80, 3 * time_per_eighth, time_per_eighth),  # A
    Note(48, 80, 4 * time_per_eighth, time_per_eighth),  # Bb
    Note(52, 80, 5 * time_per_eighth, time_per_eighth),  # C
    Note(50, 80, 6 * time_per_eighth, time_per_eighth),  # Db
    Note(53, 80, 7 * time_per_eighth, time_per_eighth),  # F
]

bass.notes.extend(bass_notes)

# ------------------
# PIANO (Diane)
# ------------------
# Chords: F7 on 2 and 4
# F7 = F, A, C, Eb
# Root position on 2 and 4, with chromatic passing on 1 and 3 (to add tension)

note_duration = 0.5  # 2 beats per chord

# Bar 1 (no chord, just chromatic passing)
# Bar 2 (F7 on beat 2)
piano.notes.append(Note(64, 90, 1 * time_per_beat, note_duration))  # F
piano.notes.append(Note(69, 90, 1 * time_per_beat, note_duration))  # A
piano.notes.append(Note(67, 90, 1 * time_per_beat, note_duration))  # C
piano.notes.append(Note(65, 90, 1 * time_per_beat, note_duration))  # Eb

# Bar 3 (no chord, chromatic passing)
# Bar 4 (F7 on beat 4)
piano.notes.append(Note(64, 90, 3 * time_per_beat, note_duration))  # F
piano.notes.append(Note(69, 90, 3 * time_per_beat, note_duration))  # A
piano.notes.append(Note(67, 90, 3 * time_per_beat, note_duration))  # C
piano.notes.append(Note(65, 90, 3 * time_per_beat, note_duration))  # Eb

# ------------------
# SAX (You)
# ------------------
# A short motif: F -> Ab -> Gb -> F (but with syncopation and space)

# First note: F (53) on beat 1, loud
sax_notes = [
    Note(53, 100, 0, 0.2),  # F at start of bar
    Note(55, 100, 0.5, 0.2),  # Ab on beat 2 (start with space)
    Note(51, 100, 1.0, 0.2),  # Gb on beat 3
    Note(53, 100, 1.5, 0.2),  # F on beat 4
]

# Make it end on a question: leave the last note hanging with a short duration
# and no resolution
sax_notes[-1].end = 1.6  # 0.1 seconds after beat 4

sax.notes.extend(sax_notes)

# Save the MIDI file
pm.write("jazz_intro_fm.mid")
print("MIDI file 'jazz_intro_fm.mid' has been created.")
