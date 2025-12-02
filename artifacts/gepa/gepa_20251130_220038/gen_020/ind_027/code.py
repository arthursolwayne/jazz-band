
import pretty_midi

# Initialize the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42
# Define note durations (in seconds)
beat_length = 0.375  # 160 BPM = 60/160 = 0.375s per beat
bar_length = 1.5     # 4 beats per bar

# BAR 1: Little Ray alone (0.0 - 1.5s)
# Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, beat_length),    # Kick on 1
    (38, beat_length, beat_length),  # Snare on 2
    (42, 0.0, beat_length / 2),     # Hihat on 1 & 2 (every eighth)
    (42, beat_length / 2, beat_length / 2),  # Hihat on 3 & 4
    (36, beat_length * 2, beat_length),    # Kick on 3
    (38, beat_length * 3, beat_length),    # Snare on 4
    (42, beat_length * 2, beat_length / 2),     # Hihat on 3 & 4
    (42, beat_length * 2.5, beat_length / 2)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# BAR 2: Full quartet (1.5 - 3.0s)
# Start of the sax motif at 1.5s
# Tenor sax: short motif in D (D-E-F#-G), start on beat 1
sax_notes = [
    (62, 1.5, beat_length),    # D (beat 1)
    (64, 1.5 + beat_length, beat_length),  # E (beat 2)
    (66, 1.5 + beat_length * 2, beat_length),  # F# (beat 3)
    (67, 1.5 + beat_length * 3, beat_length),  # G (beat 4)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: walking line in D minor (D, C, B, A, G, F#, E, D)
# Chromatic approaches
bass_notes = [
    (62, 1.5, beat_length),    # D
    (60, 1.5 + beat_length, beat_length),  # C
    (59, 1.5 + beat_length * 2, beat_length),  # B
    (67, 1.5 + beat_length * 3, beat_length),  # G (chromatic approach)
    (65, 1.5 + beat_length * 4, beat_length),  # F#
    (64, 1.5 + beat_length * 5, beat_length),  # E
    (62, 1.5 + beat_length * 6, beat_length),  # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 (D7 on 2, G7 on 4)
# D7 = D, F#, A, C
# G7 = G, B, D, F
piano_notes = [
    # D7 on beat 2 (1.5 + 0.375 = 1.875)
    (62, 1.875, beat_length),    # D
    (66, 1.875, beat_length),    # F#
    (69, 1.875, beat_length),    # A
    (60, 1.875, beat_length),    # C
    # G7 on beat 4 (1.5 + 0.375*3 = 2.25)
    (67, 2.25, beat_length),     # G
    (71, 2.25, beat_length),     # B
    (69, 2.25, beat_length),     # D
    (65, 2.25, beat_length),     # F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# BAR 3: Continue the motif and bass line
# Sax: repeat the motif starting at 3.0s
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + bar_length, end=start + duration + bar_length))

# Bass: repeat the walking line
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start + bar_length, end=start + duration + bar_length))

# Piano: repeat the same chords on 2 and 4
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start + bar_length, end=start + duration + bar_length))

# BAR 4: Continue the motif and bass line
# Sax: repeat the motif starting at 4.5s
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + bar_length * 2, end=start + duration + bar_length * 2))

# Bass: repeat the walking line
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start + bar_length * 2, end=start + duration + bar_length * 2))

# Piano: repeat the same chords on 2 and 4
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start + bar_length * 2, end=start + duration + bar_length * 2))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
