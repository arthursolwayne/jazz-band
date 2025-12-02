
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Create a sparse, tense groove with subtle fills

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=80, pitch=36, start=time, end=time + 0.15)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=60, pitch=38, start=time, end=time + 0.15)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=50, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.075)
            drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody starts, piano comps on 2 and 4, bass walks, drums continue

# Sax motif: D (D4), F# (F#4), B (B3), D (D4)
# Start on beat 1, leave it hanging on the third note
sax_note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.375)  # D4
sax_note2 = pretty_midi.Note(velocity=95, pitch=66, start=1.5 + 0.375, end=1.5 + 0.75)  # F#4
sax_note3 = pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 0.75, end=1.5 + 1.125)  # B4
sax_note4 = pretty_midi.Note(velocity=95, pitch=62, start=1.5 + 1.125, end=1.5 + 1.5)  # D4
sax.notes.extend([sax_note1, sax_note2, sax_note3, sax_note4])

# Bass line: D (D2), Eb (Eb2), F (F2), G (G2) with chromatic approach
bass_note1 = pretty_midi.Note(velocity=60, pitch=50, start=1.5, end=1.5 + 0.375)  # D2
bass_note2 = pretty_midi.Note(velocity=60, pitch=51, start=1.5 + 0.375, end=1.5 + 0.75)  # Eb2
bass_note3 = pretty_midi.Note(velocity=60, pitch=52, start=1.5 + 0.75, end=1.5 + 1.125)  # F2
bass_note4 = pretty_midi.Note(velocity=60, pitch=53, start=1.5 + 1.125, end=1.5 + 1.5)  # G2
bass.notes.extend([bass_note1, bass_note2, bass_note3, bass_note4])

# Piano: comp on 2 and 4 with 7th chords
# Bar 2, beat 2: D7 on beat 2
piano_note1 = pretty_midi.Note(velocity=80, pitch=62, start=1.5 + 0.375, end=1.5 + 0.75)  # D4
piano_note2 = pretty_midi.Note(velocity=80, pitch=67, start=1.5 + 0.375, end=1.5 + 0.75)  # B4
piano_note3 = pretty_midi.Note(velocity=80, pitch=69, start=1.5 + 0.375, end=1.5 + 0.75)  # D#4
piano_note4 = pretty_midi.Note(velocity=80, pitch=71, start=1.5 + 0.375, end=1.5 + 0.75)  # F#4

# Bar 2, beat 4: G7 on beat 4
piano_note5 = pretty_midi.Note(velocity=80, pitch=67, start=1.5 + 0.75, end=1.5 + 1.125)  # B4
piano_note6 = pretty_midi.Note(velocity=80, pitch=69, start=1.5 + 0.75, end=1.5 + 1.125)  # D#4
piano_note7 = pretty_midi.Note(velocity=80, pitch=71, start=1.5 + 0.75, end=1.5 + 1.125)  # F#4
piano_note8 = pretty_midi.Note(velocity=80, pitch=72, start=1.5 + 0.75, end=1.5 + 1.125)  # G4

piano.notes.extend([piano_note1, piano_note2, piano_note3, piano_note4, piano_note5, piano_note6, piano_note7, piano_note8])

# Bar 3: Full quartet (3.0 - 4.5s)
# Continue the groove, build tension

# Sax motif: repeat, but with a slight variation
sax_note5 = pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.0 + 0.375)  # D4
sax_note6 = pretty_midi.Note(velocity=95, pitch=66, start=3.0 + 0.375, end=3.0 + 0.75)  # F#4
sax_note7 = pretty_midi.Note(velocity=100, pitch=67, start=3.0 + 0.75, end=3.0 + 1.125)  # B4
sax_note8 = pretty_midi.Note(velocity=95, pitch=62, start=3.0 + 1.125, end=3.0 + 1.5)  # D4
sax.notes.extend([sax_note5, sax_note6, sax_note7, sax_note8])

# Bass line: D (D2), Eb (Eb2), F (F2), G (G2) with chromatic approach
bass_note5 = pretty_midi.Note(velocity=60, pitch=50, start=3.0, end=3.0 + 0.375)  # D2
bass_note6 = pretty_midi.Note(velocity=60, pitch=51, start=3.0 + 0.375, end=3.0 + 0.75)  # Eb2
bass_note7 = pretty_midi.Note(velocity=60, pitch=52, start=3.0 + 0.75, end=3.0 + 1.125)  # F2
bass_note8 = pretty_midi.Note(velocity=60, pitch=53, start=3.0 + 1.125, end=3.0 + 1.5)  # G2
bass.notes.extend([bass_note5, bass_note6, bass_note7, bass_note8])

# Piano: comp on 2 and 4 with 7th chords
# Bar 3, beat 2: D7 on beat 2
piano_note9 = pretty_midi.Note(velocity=80, pitch=62, start=3.0 + 0.375, end=3.0 + 0.75)  # D4
piano_note10 = pretty_midi.Note(velocity=80, pitch=67, start=3.0 + 0.375, end=3.0 + 0.75)  # B4
piano_note11 = pretty_midi.Note(velocity=80, pitch=69, start=3.0 + 0.375, end=3.0 + 0.75)  # D#4
piano_note12 = pretty_midi.Note(velocity=80, pitch=71, start=3.0 + 0.375, end=3.0 + 0.75)  # F#4

# Bar 3, beat 4: G7 on beat 4
piano_note13 = pretty_midi.Note(velocity=80, pitch=67, start=3.0 + 0.75, end=3.0 + 1.125)  # B4
piano_note14 = pretty_midi.Note(velocity=80, pitch=69, start=3.0 + 0.75, end=3.0 + 1.125)  # D#4
piano_note15 = pretty_midi.Note(velocity=80, pitch=71, start=3.0 + 0.75, end=3.0 + 1.125)  # F#4
piano_note16 = pretty_midi.Note(velocity=80, pitch=72, start=3.0 + 0.75, end=3.0 + 1.125)  # G4

piano.notes.extend([piano_note9, piano_note10, piano_note11, piano_note12, piano_note13, piano_note14, piano_note15, piano_note16])

# Bar 4: Full quartet (4.5 - 6.0s)
# End with a question, not a statement

# Sax motif: repeat with slight variation, leave it hanging
sax_note9 = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.5 + 0.375)  # D4
sax_note10 = pretty_midi.Note(velocity=95, pitch=66, start=4.5 + 0.375, end=4.5 + 0.75)  # F#4
sax_note11 = pretty_midi.Note(velocity=100, pitch=67, start=4.5 + 0.75, end=4.5 + 1.125)  # B4
sax_note12 = pretty_midi.Note(velocity=95, pitch=62, start=4.5 + 1.125, end=4.5 + 1.5)  # D4
sax.notes.extend([sax_note9, sax_note10, sax_note11, sax_note12])

# Bass line: D (D2), Eb (Eb2), F (F2), G (G2) with chromatic approach
bass_note9 = pretty_midi.Note(velocity=60, pitch=50, start=4.5, end=4.5 + 0.375)  # D2
bass_note10 = pretty_midi.Note(velocity=60, pitch=51, start=4.5 + 0.375, end=4.5 + 0.75)  # Eb2
bass_note11 = pretty_midi.Note(velocity=60, pitch=52, start=4.5 + 0.75, end=4.5 + 1.125)  # F2
bass_note12 = pretty_midi.Note(velocity=60, pitch=53, start=4.5 + 1.125, end=4.5 + 1.5)  # G2
bass.notes.extend([bass_note9, bass_note10, bass_note11, bass_note12])

# Piano: comp on 2 and 4 with 7th chords
# Bar 4, beat 2: D7 on beat 2
piano_note17 = pretty_midi.Note(velocity=80, pitch=62, start=4.5 + 0.375, end=4.5 + 0.75)  # D4
piano_note18 = pretty_midi.Note(velocity=80, pitch=67, start=4.5 + 0.375, end=4.5 + 0.75)  # B4
piano_note19 = pretty_midi.Note(velocity=80, pitch=69, start=4.5 + 0.375, end=4.5 + 0.75)  # D#4
piano_note20 = pretty_midi.Note(velocity=80, pitch=71, start=4.5 + 0.375, end=4.5 + 0.75)  # F#4

# Bar 4, beat 4: G7 on beat 4
piano_note21 = pretty_midi.Note(velocity=80, pitch=67, start=4.5 + 0.75, end=4.5 + 1.125)  # B4
piano_note22 = pretty_midi.Note(velocity=80, pitch=69, start=4.5 + 0.75, end=4.5 + 1.125)  # D#4
piano_note23 = pretty_midi.Note(velocity=80, pitch=71, start=4.5 + 0.75, end=4.5 + 1.125)  # F#4
piano_note24 = pretty_midi.Note(velocity=80, pitch=72, start=4.5 + 0.75, end=4.5 + 1.125)  # G4

piano.notes.extend([piano_note17, piano_note18, piano_note19, piano_note20, piano_note21, piano_note22, piano_note23, piano_note24])

# Drums continue as before
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=80, pitch=36, start=time, end=time + 0.15)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=60, pitch=38, start=time, end=time + 0.15)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=50, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.075)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("intro.mid")
