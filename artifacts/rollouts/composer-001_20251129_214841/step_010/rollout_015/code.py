
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in [0]:
    for beat in [0, 2]:  # Kick on 1 and 3
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1))
    for beat in [1, 3]:  # Snare on 2 and 4
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1))
    for beat in range(4):  # Hi-hat on every eighth
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.05))

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = []
for bar in range(1, 4):
    # C7 -> Bb -> B -> C (chromatic approach)
    bass_notes.append(pretty_midi.Note(velocity=100, pitch=60, start=bar*1.5, end=bar*1.5 + 0.375))  # C
    bass_notes.append(pretty_midi.Note(velocity=100, pitch=59, start=bar*1.5 + 0.375, end=bar*1.5 + 0.75))  # B
    bass_notes.append(pretty_midi.Note(velocity=100, pitch=60, start=bar*1.5 + 0.75, end=bar*1.5 + 1.125))  # C
    bass_notes.append(pretty_midi.Note(velocity=100, pitch=61, start=bar*1.5 + 1.125, end=bar*1.5 + 1.5))  # C#

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = []
for bar in range(1, 4):
    # Bar 2: C7 on beat 2
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=60, start=bar*1.5 + 0.75, end=bar*1.5 + 0.75 + 0.375))  # C
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=64, start=bar*1.5 + 0.75, end=bar*1.5 + 0.75 + 0.375))  # E
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=bar*1.5 + 0.75, end=bar*1.5 + 0.75 + 0.375))  # G
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=bar*1.5 + 0.75, end=bar*1.5 + 0.75 + 0.375))  # B

    # Bar 4: C7 on beat 4
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=60, start=bar*1.5 + 1.125, end=bar*1.5 + 1.125 + 0.375))  # C
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=64, start=bar*1.5 + 1.125, end=bar*1.5 + 1.125 + 0.375))  # E
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=bar*1.5 + 1.125, end=bar*1.5 + 1.125 + 0.375))  # G
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=bar*1.5 + 1.125, end=bar*1.5 + 1.125 + 0.375))  # B

piano.notes.extend(piano_notes)

# Sax: Motif in C, start on beat 1 of bar 2, leave it hanging
sax_notes = []
# Bar 2: C - E - G - B (C7 arpeggio)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.5 + 0.375))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=64, start=1.5 + 0.375, end=1.5 + 0.75))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=67, start=1.5 + 0.75, end=1.5 + 1.125))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=71, start=1.5 + 1.125, end=1.5 + 1.5))

# Bar 3: Remain silent, leave the motif hanging
# Bar 4: Return with a variation
sax_notes.append(pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.0 + 0.375))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=64, start=3.0 + 0.375, end=3.0 + 0.75))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.0 + 0.75, end=3.0 + 1.125))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=71, start=3.0 + 1.125, end=3.0 + 1.5))

sax.notes.extend(sax_notes)

# Drums: Continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1, 4):
    for beat in [0, 2]:  # Kick on 1 and 3
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1))
    for beat in [1, 3]:  # Snare on 2 and 4
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1))
    for beat in range(4):  # Hi-hat on every eighth
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.05))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
