
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
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, roots and fifths with chromatic approaches
# D - F# - A - C (Dm7)
for bar in range(2, 5):
    bass_notes = []
    if bar == 2:
        bass_notes = [38, 40, 43, 42]  # D - F# - A - C
    elif bar == 3:
        bass_notes = [42, 43, 45, 47]  # C - D - E - G
    elif bar == 4:
        bass_notes = [47, 45, 43, 42]  # G - E - D - C
    for i, note in enumerate(bass_notes):
        time = (bar - 2) * 1.5 + i * 0.375
        note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
        bass.notes.append(note_obj)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F# + C)
note = pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.5 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.5 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.5 + 0.25)
piano.notes.append(note)

# Bar 3: G7 (B + D)
note = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.0 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.0 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.0 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=3.0 + 0.25)
piano.notes.append(note)

# Bar 4: Cmaj7 (E + G)
note = pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.5 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.5 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.5 + 0.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.5 + 0.25)
piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62) - F# (66) - A (69) - D (62)
# Start on bar 2, first beat, end on bar 2, third beat
note = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.5 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=66, start=1.5 + 0.375, end=1.5 + 0.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=69, start=1.5 + 0.75, end=1.5 + 1.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=62, start=1.5 + 1.875, end=1.5 + 2.25)
sax.notes.append(note)

# Bars 2-4: Drums continue
for bar in range(2, 5):
    for beat in range(4):
        time = (bar - 2) * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
