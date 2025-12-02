
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.15)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.15)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.075)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 53, 100),  # F
    (1.875, 51, 100), # Eb
    (2.25, 55, 100),  # G
    (2.625, 57, 100), # A
    (2.875, 55, 100), # G
    (3.25, 53, 100),  # F
    (3.625, 51, 100), # Eb
    (4.0, 57, 100),   # A
    (4.375, 55, 100), # G
    (4.75, 53, 100),  # F
    (5.125, 51, 100), # Eb
    (5.5, 57, 100),   # A
    (5.875, 55, 100), # G
    (6.25, 53, 100)   # F
]
for time, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.15)
    bass.notes.append(note)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    (2.25, 64, 100),  # F
    (2.25, 69, 100),  # Bb
    (2.25, 71, 100),  # D
    (2.25, 72, 100),  # E
    # Bar 3: F7 on beat 2
    (3.625, 64, 100), # F
    (3.625, 69, 100), # Bb
    (3.625, 71, 100), # D
    (3.625, 72, 100), # E
    # Bar 4: F7 on beat 2
    (5.125, 64, 100), # F
    (5.125, 69, 100), # Bb
    (5.125, 71, 100), # D
    (5.125, 72, 100), # E
]
for time, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.15)
    piano.notes.append(note)

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.15)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.15)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.075)
            drums.notes.append(note)

# Dante on sax: one short motif, make it sing. Start it, leave it hanging, come back and finish it.
# Motif: F - Ab - Bb - F (start on beat 2 of bar 2), then rest on beat 3, then repeat ending on beat 4
sax_notes = [
    (2.25, 66, 110),  # F (beat 2 of bar 2)
    (2.625, 69, 110), # Ab
    (2.875, 71, 110), # Bb
    (3.25, 66, 110),  # F (beat 1 of bar 3)
    (3.625, 69, 110), # Ab (beat 2 of bar 3)
    (3.875, 71, 110), # Bb
    (4.125, 66, 110), # F (beat 3 of bar 3)
    (4.5, 69, 110),   # Ab (beat 1 of bar 4)
    (4.75, 71, 110),  # Bb
    (5.125, 66, 110), # F (beat 2 of bar 4)
    (5.5, 69, 110),   # Ab
    (5.75, 71, 110),  # Bb
    (6.0, 66, 110)    # F (beat 4 of bar 4)
]
for time, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.15)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.save("dante_intro.mid")
