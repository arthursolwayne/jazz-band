
import pretty_midi
import numpy as np

# Set up the MIDI file
midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
midi.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Create instruments
drums = pretty_midi.Instrument(program=10)
piano = pretty_midi.Instrument(program=0)
bass = pretty_midi.Instrument(program=33)
sax = pretty_midi.Instrument(program=64)

# Time per bar in seconds
time_per_bar = 6.0 / 4  # 1.5 seconds per bar
time_per_beat = time_per_bar / 4  # 0.375 seconds per beat

# BAR 1: DRUMS ONLY
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in [0, 2]:  # Kick on 1 and 3
        kick_time = bar * time_per_bar + beat * time_per_beat
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=kick_time, end=kick_time + 0.1))
    for beat in [1, 3]:  # Snare on 2 and 4
        snare_time = bar * time_per_bar + beat * time_per_beat
        drums.notes.append(pretty_midi.Note(velocity=95, pitch=38, start=snare_time, end=snare_time + 0.1))
    for eighth in range(8):  # Hi-hat on every eighth
        hihat_time = bar * time_per_bar + eighth * time_per_beat / 2
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.05))

# BAR 2: ALL IN
# Time for bar 2 is 1.5 seconds from bar 0 to bar 1
start_time = 1.5

# BASS LINE: Chromatic walking line, never repeating a note
bass_notes = np.array([65, 66, 67, 68, 69, 70, 71, 72])  # F to F# to G, etc.
for i in range(4):
    note_time = start_time + i * time_per_beat
    note = bass_notes[i % len(bass_notes)]
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=note_time, end=note_time + 0.25))

# PIANO: 7th chords on 2 and 4, comping
# F7 = F A C E
# F7 in root position = F A C E
# Voice leading: F -> A, A -> C, C -> E, E -> F
for i in range(4):
    if i % 2 == 0:  # On 2 and 4
        time = start_time + i * time_per_beat
        piano.notes.append(pretty_midi.Note(velocity=85, pitch=71, start=time, end=time + 0.25))  # F
        piano.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=time, end=time + 0.25))  # A
        piano.notes.append(pretty_midi.Note(velocity=75, pitch=76, start=time, end=time + 0.25))  # C
        piano.notes.append(pretty_midi.Note(velocity=70, pitch=79, start=time, end=time + 0.25))  # E

# SAX: Tenor sax — concise, emotional motif
# Motif: F (C#) - Bb - F
# In F key: F = 65, Bb = 62, C# = 67
motif = [65, 62, 67, 65]
for i, note in enumerate(motif):
    time = start_time + i * time_per_beat * 0.6  # Slightly staggered for feel
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.3))

# Add instruments to MIDI
midi.instruments = [drums, piano, bass, sax]

# Save the MIDI file
midi.write("dante_russo_intro.mid")
print("MIDI file written as 'dante_russo_intro.mid'")
