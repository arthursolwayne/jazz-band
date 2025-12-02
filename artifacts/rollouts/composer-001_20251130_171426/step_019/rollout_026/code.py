
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hi-hat on every eighth note
        note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass - walking line, chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 51, 100), (1.875, 50, 100), (2.25, 49, 100), (2.625, 51, 100),
    # Bar 3
    (3.0, 52, 100), (3.375, 51, 100), (3.75, 50, 100), (4.125, 49, 100),
    # Bar 4
    (4.5, 51, 100), (4.875, 50, 100), (5.25, 49, 100), (5.625, 51, 100)
]
for time, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.125)
    bass.notes.append(note)

# Diane on piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 on beat 1, F7 on beat 2, Bb7 on beat 3, Eb7 on beat 4
    (1.5, 72, 100), (1.875, 76, 100), (2.25, 71, 100), (2.625, 74, 100),
    # Bar 3: G7 on beat 1, C7 on beat 2, F7 on beat 3, Bb7 on beat 4
    (3.0, 76, 100), (3.375, 72, 100), (3.75, 76, 100), (4.125, 71, 100),
    # Bar 4: Bb7 on beat 1, Eb7 on beat 2, Ab7 on beat 3, Db7 on beat 4
    (4.5, 71, 100), (4.875, 74, 100), (5.25, 78, 100), (5.625, 81, 100)
]
for time, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.125)
    piano.notes.append(note)

# Little Ray on drums - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hi-hat on every eighth note
        note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Dante on sax - one short motif (C, Eb, F, Bb) - start on bar 2, beat 1
sax_notes = [
    (1.5, 65, 110), (1.875, 62, 110), (2.25, 67, 110), (2.625, 60, 110)
]
for time, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
