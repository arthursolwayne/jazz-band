
import pretty_midi
import numpy as np

# Set up the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)
instrument = pretty_midi.Instrument(program=64)  # Tenor sax
midi.instruments.append(instrument)

# Set up time parameters
time_per_bar = 1.5  # 6 seconds for 4 bars
time_per_beat = 0.375  # seconds per beat
bar_lengths = [time_per_bar] * 4

# Define note velocities and dynamics
velocities = {
    'drums': np.random.uniform(60, 100, size=10),
    'bass': np.random.uniform(60, 80, size=10),
    'piano': np.random.uniform(70, 100, size=10),
    'sax': np.random.uniform(60, 90, size=10)
}

# Define the key (F major)
F_major = [65, 67, 69, 72, 74, 76, 77]  # F, G, A, C, D, E, F#
F_minor = [65, 67, 68, 72, 74, 76, 77]  # F, G, Ab, C, D, E, F#
key = F_minor

# -- BAR 1: DRUMS ONLY (Mysterious, sparse)
# Little Ray on drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Use varying velocities and slight time shifts to create tension
bar1_start = 0.0

# Kick on 1 and 3 (slightly behind the beat)
kick_notes = [48, 48]  # C2
kick_times = [bar1_start + 0.375 * (0 + 0.1), bar1_start + 0.375 * (2 + 0.1)]
kick_velocities = velocities['drums'][0:2]

# Snare on 2 and 4 (a bit early)
snare_notes = [55, 55]  # G3
snare_times = [bar1_start + 0.375 * (1 - 0.05), bar1_start + 0.375 * (3 - 0.05)]
snare_velocities = velocities['drums'][2:4]

# Hi-hat on every eighth
hihat_notes = [42] * 8  # C1
hihat_times = [bar1_start + 0.375 * i for i in range(8)]
hihat_velocities = velocities['drums'][4:12]

# Add drum hits to the MIDI
for note, time, velocity in zip(kick_notes, kick_times, kick_velocities):
    midi.instruments[0].notes.append(pretty_midi.Note(velocity, note, time, time + 0.1))
for note, time, velocity in zip(snare_notes, snare_times, snare_velocities):
    midi.instruments[0].notes.append(pretty_midi.Note(velocity, note, time, time + 0.1))
for note, time, velocity in zip(hihat_notes, hihat_times, hihat_velocities):
    midi.instruments[0].notes.append(pretty_midi.Note(velocity, note, time, time + 0.1))

# -- BAR 2: BASS + PIANO + INTRO TO SAX
bar2_start = bar1_start + time_per_bar

# Marcus on bass: walking line, chromatic approaches, no repetition
bass_notes = [65, 67, 68, 72, 74, 76, 65, 67]  # F, G, Ab, C, D, E, F, G
bass_times = [bar2_start + 0.375 * i for i in range(8)]
bass_velocities = velocities['bass'][:8]

for note, time, velocity in zip(bass_notes, bass_times, bass_velocities):
    midi.instruments[0].notes.append(pretty_midi.Note(velocity, note, time, time + 0.1))
    
# Diane on piano: 7th chords, comp on 2 and 4, emotional, dynamic
piano_notes = [65, 72, 76, 68, 72, 76, 65, 76, 72, 76]  # F7, Ab7, F7, Ab7
piano_times = [bar2_start + 0.375 * (1.0), bar2_start + 0.375 * (1.5),
               bar2_start + 0.375 * (3.0), bar2_start + 0.375 * (3.5)]
piano_velocities = velocities['piano'][:4]

for note, time, velocity in zip(piano_notes, piano_times, piano_velocities):
    midi.instruments[0].notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# Dante on sax: sparse, expressive, start of the motif
sax_notes = [69, 72, 69, 72, 69, 65, 67]  # A, C, A, C, A, F, G
sax_times = [bar2_start + 0.375 * 0.5, bar2_start + 0.375 * 1.25,
             bar2_start + 0.375 * 1.75, bar2_start + 0.375 * 2.5,
             bar2_start + 0.375 * 2.75, bar2_start + 0.375 * 3.5,
             bar2_start + 0.375 * 3.75]
sax_velocities = velocities['sax'][:7]

for note, time, velocity in zip(sax_notes, sax_times, sax_velocities):
    midi.instruments[0].notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# -- BAR 3: RHYTHM SECTION FULL, SAX LINGERS
bar3_start = bar2_start + time_per_bar

# Drums again, slightly more aggressive
kick_notes = [48, 48]
kick_times = [bar3_start + 0.375 * (0 + 0.05), bar3_start + 0.375 * (2 + 0.05)]
kick_velocities = velocities['drums'][0:2]

snare_notes = [55, 55]
snare_times = [bar3_start + 0.375 * (1 - 0.05), bar3_start + 0.375 * (3 - 0.05)]
snare_velocities = velocities['drums'][2:4]

hihat_notes = [42] * 8
hihat_times = [bar3_start + 0.375 * i for i in range(8)]
hihat_velocities = velocities['drums'][4:12]

for note, time, velocity in zip(kick_notes, kick_times, kick_velocities):
    midi.instruments[0].notes.append(pretty_midi.Note(velocity, note, time, time + 0.1))
for note, time, velocity in zip(snare_notes, snare_times, snare_velocities):
    midi.instruments[0].notes.append(pretty_midi.Note(velocity, note, time, time + 0.1))
for note, time, velocity in zip(hihat_notes, hihat_times, hihat_velocities):
    midi.instruments[0].notes.append(pretty_midi.Note(velocity, note, time, time + 0.1))

# Bass continues the walking line
bass_notes = [65, 67, 68, 72, 74, 76, 65, 67]  # F, G, Ab, C, D, E, F, G
bass_times = [bar3_start + 0.375 * i for i in range(8)]
bass_velocities = velocities['bass'][8:16]

for note, time, velocity in zip(bass_notes, bass_times, bass_velocities):
    midi.instruments[0].notes.append(pretty_midi.Note(velocity, note, time, time + 0.1))

# Piano more active, tension builds
piano_notes = [65, 76, 69, 68, 72, 65, 67, 76]  # F7, E7, A7, Ab7, C7, F7, G7, E7
piano_times = [bar3_start + 0.375 * (1.0), bar3_start + 0.375 * (1.5),
               bar3_start + 0.375 * (2.0), bar3_start + 0.375 * (2.5),
               bar3_start + 0.375 * (3.0), bar3_start + 0.375 * (3.5),
               bar3_start + 0.375 * (3.75), bar3_start + 0.375 * (4.0)]
piano_velocities = velocities['piano'][4:12]

for note, time, velocity in zip(piano_notes, piano_times, piano_velocities):
    midi.instruments[0].notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# Sax continues the motif, slightly more resolved
sax_notes = [69, 72, 76, 69, 65, 67, 69]  # A, C, E, A, F, G, A
sax_times = [bar3_start + 0.375 * 0.5, bar3_start + 0.375 * 1.25,
             bar3_start + 0.375 * 1.75, bar3_start + 0.375 * 2.5,
             bar3_start + 0.375 * 2.75, bar3_start + 0.375 * 3.5,
             bar3_start + 0.375 * 3.75]
sax_velocities = velocities['sax'][7:14]

for note, time, velocity in zip(sax_notes, sax_times, sax_velocities):
    midi.instruments[0].notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# -- BAR 4: TENSION CULMINATES, PIANO DECIDES IT
bar4_start = bar3_start + time_per_bar

# Drums again, final push
kick_notes = [48, 48]
kick_times = [bar4_start + 0.375 * (0 + 0.05), bar4_start + 0.375 * (2 + 0.05)]
kick_velocities = velocities['drums'][0:2]

snare_notes = [55, 55]
snare_times = [bar4_start + 0.375 * (1 - 0.05), bar4_start + 0.375 * (3 - 0.05)]
snare_velocities = velocities['drums'][2:4]

hihat_notes = [42] * 8
hihat_times = [bar4_start + 0.375 * i for i in range(8)]
hihat_velocities = velocities['drums'][4:12]

for note, time, velocity in zip(kick_notes, kick_times, kick_velocities):
    midi.instruments[0].notes.append(pretty_midi.Note(velocity, note, time, time + 0.1))
for note, time, velocity in zip(snare_notes, snare_times, snare_velocities):
    midi.instruments[0].notes.append(pretty_midi.Note(velocity, note, time, time + 0.1))
for note, time, velocity in zip(hihat_notes, hihat_times, hihat_velocities):
    midi.instruments[0].notes.append(pretty_midi.Note(velocity, note, time, time + 0.1))

# Bass ends the line, resolves on a G
bass_notes = [67]  # G
bass_times = [bar4_start + 0.375 * 3.0]
bass_velocities = velocities['bass'][16:17]

for note, time, velocity in zip(bass_notes, bass_times, bass_velocities):
    midi.instruments[0].notes.append(pretty_midi.Note(velocity, note, time, time + 0.1))

# Piano resolves with a dissonant G7 chord
piano_notes = [67, 76, 72, 74]  # G7
piano_times = [bar4_start + 0.375 * (1.0), bar4_start + 0.375 * (1.5),
               bar4_start + 0.375 * (2.5), bar4_start + 0.375 * (3.0)]
piano_velocities = velocities['piano'][12:16]

for note, time, velocity in zip(piano_notes, piano_times, piano_velocities):
    midi.instruments[0].notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# Sax ends on a lingering note with space
sax_notes = [69]  # A
sax_times = [bar4_start + 0.375 * 3.5]
sax_velocities = velocities['sax'][14:15]

for note, time, velocity in zip(sax_notes, sax_times, sax_velocities):
    midi.instruments[0].notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# Save the MIDI file
midi.write("jazz_intro.mid")
