
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_duration = 1.5
for i in range(4):
    time = i * bar_duration / 4
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + bar_duration / 4)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=time + bar_duration / 2, end=time + bar_duration / 2 + bar_duration / 4)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + bar_duration / 2)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time + bar_duration / 2, end=time + bar_duration)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    (17, 1.5), (19, 1.75), (20, 2.0), (22, 2.25),
    (17, 2.5), (19, 2.75), (20, 3.0), (22, 3.25),
    (17, 3.5), (19, 3.75), (20, 4.0), (22, 4.25),
    (17, 4.5), (19, 4.75), (20, 5.0), (22, 5.25)
]
for pitch, start in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: open voicings, different chord each bar, resolve on the last
chords = [
    [17, 22, 24, 26],     # Fmaj7
    [18, 22, 24, 27],     # Gm7
    [17, 21, 23, 26],     # Dm7
    [18, 22, 24, 27]      # Gm7 (resolve)
]
for i, chord in enumerate(chords):
    start = 1.5 + i * bar_duration
    for pitch in chord:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.5)
        piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65) - A (69) - D (62) - F (65)
# Bar 2: Start motif on 1
note = pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.6)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=69, start=1.6, end=1.7)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=62, start=1.7, end=1.8)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=65, start=1.8, end=1.9)
sax.notes.append(note)

# Bar 3: Let it hang, then come back with the motif
note = pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.1)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=69, start=3.1, end=3.2)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=62, start=3.2, end=3.3)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=65, start=3.3, end=3.4)
sax.notes.append(note)

# Bar 4: End with a strong resolution
note = pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.6)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=69, start=4.6, end=4.7)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=62, start=4.7, end=4.8)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=65, start=4.8, end=5.0)
sax.notes.append(note)

# Drums: Continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth for bars 2-4
for bar in range(2, 4):
    for i in range(4):
        time = 1.5 + bar * bar_duration + i * bar_duration / 4
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + bar_duration / 4)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=38, start=time + bar_duration / 2, end=time + bar_duration / 2 + bar_duration / 4)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + bar_duration / 2)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time + bar_duration / 2, end=time + bar_duration)
        drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
