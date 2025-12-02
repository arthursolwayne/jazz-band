
import pretty_midi

# Setup
tempo = 160  # BPM
time_signature = (4, 4)
key = 'Dm'  # D minor

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=tempo, time_signature=(4, 4))

# Define note values and time
note_duration = 0.375  # 1/8 note at 160 BPM
bar_length = 1.5  # 4/4 bar at 160 BPM
total_length = 6.0  # 4 bars

# Create instruments
drums = pretty_midi.Instrument(program=10)  # Drums
sax = pretty_midi.Instrument(program=64)    # Tenor sax
piano = pretty_midi.Instrument(program=0)   # Piano
bass = pretty_midi.Instrument(program=33)   # Electric bass

pm.instruments = [drums, sax, piano, bass]

# Drum pattern (Bar 1: Little Ray alone)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# We'll use MIDI note numbers:
# Kick: 36, Snare: 38, Hihat: 42

bar1_start = 0.0
bar1_end = 1.5

# Hihat every 1/8 note
for i in range(0, 8):
    hihat_time = bar1_start + i * note_duration
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.1)
    drums.notes.append(hihat)

# Kick on 1 and 3
kick_times = [bar1_start, bar1_start + 2 * note_duration]
for kick_time in kick_times:
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)

# Snare on 2 and 4
snare_times = [bar1_start + note_duration, bar1_start + 4 * note_duration]
for snare_time in snare_times:
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)

# Bar 2: All instruments in
bar2_start = 1.5
bar2_end = 3.0

# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Dm7: D, F, A, C
    # Chromatic approach to D (C#), then D
    (37, bar2_start + 0 * note_duration, 0.1),   # C#
    (37, bar2_start + 1 * note_duration, 0.1),   # D
    (38, bar2_start + 2 * note_duration, 0.1),   # Eb
    (38, bar2_start + 3 * note_duration, 0.1),   # E
    (40, bar2_start + 4 * note_duration, 0.1),   # F
    (40, bar2_start + 5 * note_duration, 0.1),   # F
    (42, bar2_start + 6 * note_duration, 0.1),   # G
    (42, bar2_start + 7 * note_duration, 0.1),   # G
]

for pitch, start, dur in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + dur)
    bass.notes.append(note)

# Piano comp: 7th chords on 2 and 4, with some tension
# Dm7: D, F, A, C
# 7th chord at bar2_start + 1 * note_duration (beat 2)
# Add a Bb for tension

# Beat 2 (bar2_start + 1 * note_duration)
piano_notes = [
    (50, bar2_start + 1 * note_duration, 0.5),   # D
    (53, bar2_start + 1 * note_duration, 0.5),   # F
    (57, bar2_start + 1 * note_duration, 0.5),   # A
    (60, bar2_start + 1 * note_duration, 0.5),   # C
    (59, bar2_start + 1 * note_duration, 0.5),   # Bb (tension)
]

# Beat 4 (bar2_start + 3 * note_duration)
piano_notes += [
    (50, bar2_start + 3 * note_duration, 0.5),   # D
    (53, bar2_start + 3 * note_duration, 0.5),   # F
    (57, bar2_start + 3 * note_duration, 0.5),   # A
    (60, bar2_start + 3 * note_duration, 0.5),   # C
    (59, bar2_start + 3 * note_duration, 0.5),   # Bb
]

for pitch, start, dur in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + dur)
    piano.notes.append(note)

# Tenor sax melody: short motif, searching, not repeating
# Dm scale: D, Eb, F, G, A, Bb, C
# Melody: D -> Eb (question) -> F (resolution) -> Bb (tension)
# Leave it hanging

sax_notes = [
    (50, bar2_start, 0.5),     # D
    (51, bar2_start + 0.5, 0.5), # Eb
    (53, bar2_start + 1.0, 0.5), # F
    (59, bar2_start + 1.5, 0.5), # Bb
]

for pitch, start, dur in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + dur)
    sax.notes.append(note)

# Write the MIDI file
pm.write("dante_intro.mid")

print("MIDI file 'dante_intro.mid' created successfully.")
