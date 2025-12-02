
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
        if beat in [0, 2]:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat in [1, 3]:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
# Dm7: D F A C
bass_notes = [50, 51, 53, 55, 57, 58, 60, 62]
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        note = pretty_midi.Note(velocity=80, pitch=bass_notes[(bar - 2) * 4 + beat], start=time, end=time + 0.25)
        bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Dm7 = D F A C
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat in [1, 3]:
            note1 = pretty_midi.Note(velocity=90, pitch=50, start=time, end=time + 0.25)
            note2 = pretty_midi.Note(velocity=90, pitch=53, start=time, end=time + 0.25)
            note3 = pretty_midi.Note(velocity=90, pitch=55, start=time, end=time + 0.25)
            note4 = pretty_midi.Note(velocity=90, pitch=57, start=time, end=time + 0.25)
            piano.notes.append(note1)
            piano.notes.append(note2)
            piano.notes.append(note3)
            piano.notes.append(note4)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm: D F A C
# Motif: D -> F -> A -> C -> D (but missing the last D)
# Use quarter notes, start on beat 1 of bar 2 and end on beat 3 of bar 2
note1 = pretty_midi.Note(velocity=110, pitch=50, start=1.5, end=1.875)
note2 = pretty_midi.Note(velocity=110, pitch=53, start=1.875, end=2.25)
note3 = pretty_midi.Note(velocity=110, pitch=55, start=2.25, end=2.625)
note4 = pretty_midi.Note(velocity=110, pitch=57, start=2.625, end=3.0)
sax.notes.append(note1)
sax.notes.append(note2)
sax.notes.append(note3)
sax.notes.append(note4)

# Repeat the motif at the end of bar 4
note5 = pretty_midi.Note(velocity=110, pitch=50, start=4.5, end=4.875)
note6 = pretty_midi.Note(velocity=110, pitch=53, start=4.875, end=5.25)
note7 = pretty_midi.Note(velocity=110, pitch=55, start=5.25, end=5.625)
note8 = pretty_midi.Note(velocity=110, pitch=57, start=5.625, end=6.0)
sax.notes.append(note5)
sax.notes.append(note6)
sax.notes.append(note7)
sax.notes.append(note8)

midi.instruments.extend([sax, bass, piano, drums])
