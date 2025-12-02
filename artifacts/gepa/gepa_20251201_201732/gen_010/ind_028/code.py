
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
        note = pretty_midi.Note(velocity=70, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line in Fm (F2, G2, Ab2, A2, Bb2, B2, C2)
# Roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.625),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.0),  # G2
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.375), # Ab2
    pretty_midi.Note(velocity=90, pitch=54, start=2.625, end=2.75), # A2
    pretty_midi.Note(velocity=90, pitch=51, start=2.875, end=3.0),  # Bb2
    pretty_midi.Note(velocity=90, pitch=53, start=3.125, end=3.25), # F2
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.5),  # G2
    pretty_midi.Note(velocity=90, pitch=52, start=3.625, end=3.75), # Ab2
    pretty_midi.Note(velocity=90, pitch=54, start=3.875, end=4.0),  # A2
    pretty_midi.Note(velocity=90, pitch=51, start=4.125, end=4.25), # Bb2
    pretty_midi.Note(velocity=90, pitch=53, start=4.375, end=4.5),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=4.625, end=4.75), # G2
    pretty_midi.Note(velocity=90, pitch=52, start=4.875, end=5.0),  # Ab2
    pretty_midi.Note(velocity=90, pitch=54, start=5.125, end=5.25), # A2
    pretty_midi.Note(velocity=90, pitch=51, start=5.375, end=5.5),  # Bb2
]
bass.notes.extend(bass_notes)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
note = pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75)
piano.notes.append(note)

# Bar 3: Bb7 (Bb, D, F, Ab)
note = pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.5)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=54, start=2.25, end=2.5)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.5)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.5)
piano.notes.append(note)

# Bar 4: Cm7 (C, Eb, G, Bb)
note = pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=54, start=3.0, end=3.25)
piano.notes.append(note)

# Little Ray on drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=70, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, F
note = pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.625)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=55, start=1.625, end=1.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=51, start=1.75, end=1.875)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=53, start=2.0, end=2.125)
sax.notes.append(note)

# End of piece
midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
