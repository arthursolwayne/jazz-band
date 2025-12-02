
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
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        hihat_time = time + 0.1875
        note = pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.0625)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Sax: One short motif, start it, leave it hanging, come back and finish it
# F7 chord: F, A, C, E
# Motif: F - E - D - F (1st bar of melody)
# Leave it hanging on D, finish it on F in the third bar

# Bar 2 (1.5 - 3.0s)
note = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625)  # F
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875)  # E
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.125)   # D
sax.notes.append(note)

# Bar 3 (3.0 - 4.5s) - bass walks, piano comps with 7th chords
# Bass: F, Gb, G, Ab (chromatic walk)
note = pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.125)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=63, start=3.375, end=3.5)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=3.875)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=66, start=4.125, end=4.25)
bass.notes.append(note)

# Piano: 7th chords on 2 and 4
note = pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.5)  # F7 (F, A, C, E)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.5)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.5)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.5)
piano.notes.append(note)

note = pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.25)
piano.notes.append(note)

# Bar 3 (3.0 - 4.5s) - Sax continues motif
note = pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.125)  # F
sax.notes.append(note)

# Bar 4 (4.5 - 6.0s) - Sax finishes motif, everyone resolves
note = pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.625)  # F
sax.notes.append(note)

# Bass continues walking
note = pretty_midi.Note(velocity=80, pitch=68, start=4.5, end=4.625)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.0)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=70, start=5.25, end=5.375)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=5.75)
bass.notes.append(note)

# Piano resolves with F7 on beat 4
note = pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=5.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=5.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=5.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=5.75)
piano.notes.append(note)

# Drums continue
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        hihat_time = time + 0.1875
        note = pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.0625)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
