
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante on Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Marcus on Bass
piano = pretty_midi.Instrument(program=0)      # Diane on Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray on Drums

# Drum MIDI note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Time in seconds: bar 1 is 0.0 to 1.5
bar_length = 1.5
beat_length = bar_length / 4  # 0.375 seconds per beat

# Fill the bar with a driving groove
for beat in range(4):
    time = beat * beat_length
    if beat in [0, 2]:  # Kick on 1 and 3
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.1))
    if beat in [1, 3]:  # Snare on 2 and 4
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.1))
    for eighth in [0, 1]:  # Hihat on every eighth
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.05))

# Bar 2: Full quartet (1.5 - 3.0s)
# Diane on piano: 7th chords, comp on 2 and 4

# Fm7 chord: F, Ab, C, Eb
# Diane plays on 2 and 4
for beat in [1, 3]:
    time = 1.5 + beat * beat_length
    # Fm7 chord: root + 7th + 9th (if possible)
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=87, start=time, end=time + 0.25))  # F
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=time, end=time + 0.25))  # Ab
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=81, start=time, end=time + 0.25))  # C
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=time, end=time + 0.25))  # Eb

# Marcus on bass: walking line with chromatic approaches
# Fm7 walking line: F, Gb, Ab, A
# Bars 2-4: 8 bars total, but we're in bar 2 here (1.5 - 3.0s)
bass_notes = [77, 76, 79, 80]  # F, Gb, Ab, A
for i, note in enumerate(bass_notes):
    time = 1.5 + i * beat_length
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Dante on sax: short motif, make it sing. Start it, leave it hanging, come back and finish it
# Motif: F (C4), Ab (D4), Bb (E4), F (C4) — a simple, angular line
# Start on the "and" of 1, leave it hanging at the end of the bar

# F (C4) on 1 & (time = 1.5 + 0.1875)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=1.5 + 0.1875, end=1.5 + 0.375))
# Ab (D4) on 2 (time = 1.5 + 0.375)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=1.5 + 0.375, end=1.5 + 0.75))
# Bb (E4) on 3 (time = 1.5 + 0.75)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=81, start=1.5 + 0.75, end=1.5 + 1.125))
# F (C4) on 4 (time = 1.5 + 1.125)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=1.5 + 1.125, end=1.5 + 1.5))  # End on beat 4

# Bar 3: Full quartet (3.0 - 4.5s)
# Diane on piano: 7th chords, comp on 2 and 4
for beat in [1, 3]:
    time = 3.0 + beat * beat_length
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=87, start=time, end=time + 0.25))  # F
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=time, end=time + 0.25))  # Ab
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=81, start=time, end=time + 0.25))  # C
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=time, end=time + 0.25))  # Eb

# Marcus on bass: walking line, chromatic approaches
# Fm7 walking line: F, Gb, Ab, A
for i, note in enumerate(bass_notes):
    time = 3.0 + i * beat_length
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Dante on sax: repeat the motif now, starting on beat 1
# F (C4) on 1 (time = 3.0)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.0 + 0.375))
# Ab (D4) on 2 (time = 3.0 + 0.375)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=3.0 + 0.375, end=3.0 + 0.75))
# Bb (E4) on 3 (time = 3.0 + 0.75)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=81, start=3.0 + 0.75, end=3.0 + 1.125))
# F (C4) on 4 (time = 3.0 + 1.125)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=3.0 + 1.125, end=3.0 + 1.5))

# Bar 4: Full quartet (4.5 - 6.0s)
# Diane on piano: 7th chords, comp on 2 and 4
for beat in [1, 3]:
    time = 4.5 + beat * beat_length
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=87, start=time, end=time + 0.25))  # F
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=time, end=time + 0.25))  # Ab
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=81, start=time, end=time + 0.25))  # C
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=time, end=time + 0.25))  # Eb

# Marcus on bass: walking line
for i, note in enumerate(bass_notes):
    time = 4.5 + i * beat_length
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Little Ray: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = 4.5 + beat * beat_length
    if beat in [0, 2]:  # Kick on 1 and 3
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.1))
    if beat in [1, 3]:  # Snare on 2 and 4
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.1))
    for eighth in [0, 1]:  # Hihat on every eighth
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.05))

# Add the instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_intro.mid")
