
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
for beat in [0, 2]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)
for beat in [1, 3]:
    note = pretty_midi.Note(velocity=100, pitch=38, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)
for beat in range(4):
    note = pretty_midi.Note(velocity=80, pitch=42, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass line: Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 70, 38), (1.75, 72, 40), (2.0, 70, 38), (2.25, 69, 37),
    (2.5, 70, 38), (2.75, 72, 40), (3.0, 70, 38), (3.25, 69, 37),
    (3.5, 70, 38), (3.75, 72, 40), (4.0, 70, 38), (4.25, 69, 37),
    (4.5, 70, 38), (4.75, 72, 40), (5.0, 70, 38), (5.25, 69, 37)
]
for start, vel, pitch in bass_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F A C E)
note = pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.75)
piano.notes.append(note)

# Bar 3: Bb7 (Bb D F Ab)
note = pretty_midi.Note(velocity=100, pitch=70, start=2.5, end=2.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=2.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=77, start=2.5, end=2.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=80, start=2.5, end=2.75)
piano.notes.append(note)

# Bar 4: Cm7 (C Eb G Bb)
note = pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=3.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=79, start=3.5, end=3.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=80, start=3.5, end=3.75)
piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F (72), Bb (70), C (72), G (75), F (72)
note = pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=70, start=1.75, end=2.0)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=75, start=2.25, end=2.5)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.75)
sax.notes.append(note)

# Drums for bars 2-4
for beat in range(4):
    note = pretty_midi.Note(velocity=100, pitch=36, start=(1.5 + beat * 0.375), end=(1.5 + beat * 0.375) + 0.25)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=(1.5 + (beat + 1) * 0.375), end=(1.5 + (beat + 1) * 0.375) + 0.25)
    drums.notes.append(note)
    for eighth in range(2):
        note = pretty_midi.Note(velocity=80, pitch=42, start=(1.5 + beat * 0.375 + eighth * 0.1875), end=(1.5 + beat * 0.375 + eighth * 0.1875) + 0.1875)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
