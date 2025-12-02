
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
bar_length = 1.5
for i in range(4):
    time = i * bar_length / 4
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + bar_length / 4)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=time + bar_length / 2, end=time + bar_length / 2 + bar_length / 4)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + bar_length / 4)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 37), (1.75, 39), (2.0, 40), (2.25, 37),
    (2.5, 39), (2.75, 40), (3.0, 41), (3.25, 37),
    (3.5, 39), (3.75, 40), (4.0, 41), (4.25, 37),
    (4.5, 39), (4.75, 40), (5.0, 41), (5.25, 37)
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
chords = [
    # Bar 2: Fmaj7
    (1.5, 60, 64, 67, 71),
    # Bar 3: Bb7
    (2.5, 62, 66, 69, 73),
    # Bar 4: Cm7
    (3.5, 57, 60, 64, 68)
]
for i, chord in enumerate(chords):
    time = 1.5 + i * bar_length
    for pitch in chord:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + bar_length / 2)
        piano.notes.append(note)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 62), (1.75, 66), (2.0, 62), (2.25, 66),
    (3.5, 62), (3.75, 66), (4.0, 62), (4.25, 66),
    (5.5, 62), (5.75, 66), (6.0, 62)
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    time = 1.5 + i * bar_length
    for j in range(4):
        kick_time = time + j * bar_length / 4
        note = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + bar_length / 4)
        drums.notes.append(note)
        snare_time = time + j * bar_length / 4 + bar_length / 2
        note = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + bar_length / 4)
        drums.notes.append(note)
        for k in range(4):
            hihat_time = time + j * bar_length / 4 + k * bar_length / 4
            note = pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + bar_length / 8)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
