
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante - Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Marcus - Bass
piano = pretty_midi.Instrument(program=0)      # Diane - Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray - Drums

# MIDI note numbers
# Fm7 chord: F (65), Ab (69), C (67), D (62) - but we'll use 7th chords with chromatic motion
# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    time = bar * 1.5
    # Kick on 1 and 3 (beats 0 and 2 within the bar)
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time + beat * 0.375, end=time + beat * 0.375 + 0.125)
        drums.notes.append(note)
    # Snare on 2 and 4 (beats 1 and 3)
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time + beat * 0.375, end=time + beat * 0.375 + 0.125)
        drums.notes.append(note)
    # Hihat on every eighth (beats 0-3)
    for beat in range(4):
        note = pretty_midi.Note(velocity=80, pitch=42, start=time + beat * 0.375, end=time + beat * 0.375 + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Start at bar 2 (time = 1.5s)

# Marcus on bass: Walking line, chromatic approaches, no repeated notes
# Fm7 (F, Ab, C, D) -> walking line: F, Gb, G, Ab, A, Bb, B, C, D, Eb, E, F
bass_notes = [65, 66, 67, 69, 70, 71, 72, 67, 69, 71, 72, 65]
bass_beats = [0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625, 3, 3.375, 3.75, 4.125]
for i in range(len(bass_notes)):
    note = pretty_midi.Note(velocity=80, pitch=bass_notes[i], start=1.5 + bass_beats[i], end=1.5 + bass_beats[i] + 0.125)
    bass.notes.append(note)

# Diane on piano: 7th chords, comp on 2 and 4
# Fm7 on beat 1 and 3 (bars 2 and 4)
# Fm7: F (65), Ab (69), C (67), D (62)
for bar in [2, 4]:
    time = 1.5 + (bar - 2) * 1.5
    for beat in [0, 2]:
        # Fm7 chord: F, Ab, C, D
        for pitch in [65, 69, 67, 62]:
            note = pretty_midi.Note(velocity=90, pitch=pitch, start=time + beat * 0.375, end=time + beat * 0.375 + 0.125)
            piano.notes.append(note)

# Little Ray on drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    time = 1.5 + (bar - 2) * 1.5
    # Kick on 1 and 3 (beats 0 and 2)
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time + beat * 0.375, end=time + beat * 0.375 + 0.125)
        drums.notes.append(note)
    # Snare on 2 and 4 (beats 1 and 3)
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time + beat * 0.375, end=time + beat * 0.375 + 0.125)
        drums.notes.append(note)
    # Hihat on every eighth (beats 0-3)
    for beat in range(4):
        note = pretty_midi.Note(velocity=80, pitch=42, start=time + beat * 0.375, end=time + beat * 0.375 + 0.125)
        drums.notes.append(note)

# Dante on sax: The motif. One short phrase, sing it, leave it hanging.
# Start with a short motif: F (65), Ab (69), F (65), Eb (64)
# Then leave it hanging on the last beat of bar 2
# Then come back with the same motif in bar 3, completing the phrase
# Bar 2, beat 0: F
note = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.5 + 0.125)
sax.notes.append(note)
# Bar 2, beat 1: Ab
note = pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=1.875 + 0.125)
sax.notes.append(note)
# Bar 2, beat 2: F (return)
note = pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.25 + 0.125)
sax.notes.append(note)
# Bar 2, beat 3: Eb (leave it hanging)
note = pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0)  # ends on 3.0 (beat 4)
sax.notes.append(note)
# Bar 3, beat 0: F (come back)
note = pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.0 + 0.125)
sax.notes.append(note)
# Bar 3, beat 1: Ab
note = pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.375 + 0.125)
sax.notes.append(note)
# Bar 3, beat 2: F (complete the motif)
note = pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=3.75 + 0.125)
sax.notes.append(note)
# Bar 3, beat 3: Eb (end on it)
note = pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5)
sax.notes.append(note)

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
