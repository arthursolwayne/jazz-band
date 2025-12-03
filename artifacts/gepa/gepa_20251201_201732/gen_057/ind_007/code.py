
import pretty_midi
from pretty_midi import Note, Instrument

# Set tempo and time signature
tempo = 160  # BPM
time_signature = (4, 4)

# Create a new MIDI file
midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(*time_signature, 0.0)]
midi.tempos = [pretty_midi.TempoChange(tempo, 0.0)]

# Define instruments
bass_program = pretty_midi.instrument_name_to_program("Acoustic Bass")
piano_program = pretty_midi.instrument_name_to_program("Electric Piano 1")
drums_program = pretty_midi.instrument_name_to_program("Acoustic Drums")
sax_program = pretty_midi.instrument_name_to_program("Tenor Saxophone")

# Create instruments
bass = Instrument(program=bass_program)
piano = Instrument(program=piano_program)
drums = Instrument(program=drums_program)
sax = Instrument(program=sax_program)

# Add instruments to MIDI
midi.instruments = [bass, piano, drums, sax]

# CREATE BAR 1: DRUMS ONLY — TENSION, HAUNTING, SUBTLE

# Bar 1: 6 beats (4/4 time, 6 seconds at 160 BPM)
# Little Ray — kick on 1 and 3, snare on 2 and 4, hihat every eighth
# Time per beat: 0.375s, time per eighth: 0.1875s

bar1_start = 0.0
bar1_end = 1.5  # 6 seconds total / 4 bars = 1.5s per bar

# Kick on 1 and 3
kick_times = [bar1_start + 0.0, bar1_start + 0.75]
kick_notes = [36] * len(kick_times)

# Snare on 2 and 4
snare_times = [bar1_start + 0.375, bar1_start + 1.125]
snare_notes = [38] * len(snare_times)

# Hihat on every eighth note
hihat_times = [bar1_start + i * 0.1875 for i in range(8)]
hihat_notes = [42] * len(hihat_times)

# Add to drums
for time, note in zip(kick_times, kick_notes):
    drums.notes.append(Note(note, time, time + 0.125))

for time, note in zip(snare_times, snare_notes):
    drums.notes.append(Note(note, time, time + 0.125))

for time, note in zip(hihat_times, hihat_notes):
    drums.notes.append(Note(note, time, time + 0.0625))

# BAR 2: EVERYONE IN — INTRO LINE FROM SAX, PIANO VOICINGS, BASS WALK

# Bar 2 starts at 1.5s
bar2_start = 1.5
bar2_end = 3.0

# SAX: One short motif — concise, expressive
# D (D4) -> F# (F#4) -> B (B4) -> A (A4) — leave it hanging on the third beat
# Time: bar2_start + 0.0, 0.375, 0.75, 1.125
sax_notes = [62, 66, 71, 69]  # D4, F#4, B4, A4
sax_times = [bar2_start + 0.0, bar2_start + 0.375, bar2_start + 0.75, bar2_start + 1.125]
sax_durations = [0.25, 0.25, 0.25, 0.25]

for time, note, duration in zip(sax_times, sax_notes, sax_durations):
    sax.notes.append(Note(note, time, time + duration))

# PIANO: Open voicings, different chord each bar, resolve on last
# Bar 2: D7 (D F# A C#) — open voicing
# D (62), F# (66), A (70), C# (73)
piano_notes = [62, 66, 70, 73]
piano_times = [bar2_start + 0.0, bar2_start + 0.0, bar2_start + 0.0, bar2_start + 0.0]
piano_durations = [1.5] * 4  # For space and sustain

# But play only on beats 2 and 4
for i, note in enumerate(piano_notes):
    piano.notes.append(Note(note, bar2_start + 0.375 + i * 0.75, bar2_start + 0.375 + i * 0.75 + 0.5))

# BASS: Walking line in D, roots and fifths, chromatic approach
# D2 (38), A2 (43), D2 (38), chromatic approach to F#2 (44)
bass_notes = [38, 43, 38, 44]
bass_times = [bar2_start + 0.0, bar2_start + 0.75, bar2_start + 1.5, bar2_start + 2.25]
bass_durations = [0.25] * 4

for time, note, duration in zip(bass_times, bass_notes, bass_durations):
    bass.notes.append(Note(note, time, time + duration))

# BAR 3: CONTINUATION — BASS, PIANO, SAX (IMPLICIT GESTURE)
bar3_start = 3.0
bar3_end = 4.5

# PIANO: D7 again but now on beat 4
piano_notes = [62, 66, 70, 73]
piano_times = [bar3_start + 0.0, bar3_start + 0.0, bar3_start + 0.0, bar3_start + 0.0]
piano_durations = [1.5] * 4

for i, note in enumerate(piano_notes):
    piano.notes.append(Note(note, bar3_start + 0.375 + i * 0.75, bar3_start + 0.375 + i * 0.75 + 0.5))

# BASS: Walk again, D2, A2, D2, F#2
bass_notes = [38, 43, 38, 44]
bass_times = [bar3_start + 0.0, bar3_start + 0.75, bar3_start + 1.5, bar3_start + 2.25]
bass_durations = [0.25] * 4

for time, note, duration in zip(bass_times, bass_notes, bass_durations):
    bass.notes.append(Note(note, time, time + duration))

# BAR 4: RESOLUTION — SAX COMPLETES THE LINE, PIANO D7
bar4_start = 4.5
bar4_end = 6.0

# SAX: Return to the motif, finish the phrase
# D4, F#4, B4, A4 — but now, a slight release on the last note
sax_notes = [62, 66, 71, 69]
sax_times = [bar4_start + 0.0, bar4_start + 0.375, bar4_start + 0.75, bar4_start + 1.125]
sax_durations = [0.25, 0.25, 0.25, 0.25]

for time, note, duration in zip(sax_times, sax_notes, sax_durations):
    sax.notes.append(Note(note, time, time + duration))

# PIANO: D7 on beat 4
piano_notes = [62, 66, 70, 73]
piano_times = [bar4_start + 0.0, bar4_start + 0.0, bar4_start + 0.0, bar4_start + 0.0]
piano_durations = [1.5] * 4

for i, note in enumerate(piano_notes):
    piano.notes.append(Note(note, bar4_start + 0.375 + i * 0.75, bar4_start + 0.375 + i * 0.75 + 0.5))

# BASS: Walk again, but resolve back to D
bass_notes = [38, 43, 38, 38]
bass_times = [bar4_start + 0.0, bar4_start + 0.75, bar4_start + 1.5, bar4_start + 2.25]
bass_durations = [0.25] * 4

for time, note, duration in zip(bass_times, bass_notes, bass_durations):
    bass.notes.append(Note(note, time, time + duration))

# Add drum fills for bar 4
# Kick on 1 and 3
kick_times = [bar4_start + 0.0, bar4_start + 0.75]
kick_notes = [36] * len(kick_times)

# Snare on 2 and 4
snare_times = [bar4_start + 0.375, bar4_start + 1.125]
snare_notes = [38] * len(snare_times)

# Hihat on every eighth note
hihat_times = [bar4_start + i * 0.1875 for i in range(8)]
hihat_notes = [42] * len(hihat_times)

# Add to drums
for time, note in zip(kick_times, kick_notes):
    drums.notes.append(Note(note, time, time + 0.125))

for time, note in zip(snare_times, snare_notes):
    drums.notes.append(Note(note, time, time + 0.125))

for time, note in zip(hihat_times, hihat_notes):
    drums.notes.append(Note(note, time, time + 0.0625))

# Save the MIDI file
# midi.write disabled
