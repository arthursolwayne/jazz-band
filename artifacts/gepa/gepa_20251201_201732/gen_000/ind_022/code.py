
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
for beat in [0, 1, 2, 3]:
    note = pretty_midi.Note(velocity=100, pitch=42, start=beat * 0.375, end=beat * 0.375 + 0.125)
    drums.notes.append(note)
for beat in [0, 2]:
    note = pretty_midi.Note(velocity=110, pitch=38, start=beat * 0.375, end=beat * 0.375 + 0.125)
    drums.notes.append(note)
for beat in [0, 1, 2, 3]:
    note = pretty_midi.Note(velocity=80, pitch=36, start=beat * 0.375, end=beat * 0.375 + 0.125)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: D4 -> F#4 -> A4 -> B4 -> A4 -> F#4 -> D4 (motif)
sax_note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.375)
sax_note2 = pretty_midi.Note(velocity=100, pitch=66, start=1.5 + 0.375, end=1.5 + 0.75)
sax_note3 = pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 0.75, end=1.5 + 1.125)
sax_note4 = pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 1.125, end=1.5 + 1.5)
sax_note5 = pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 1.5, end=1.5 + 1.875)
sax_note6 = pretty_midi.Note(velocity=100, pitch=66, start=1.5 + 1.875, end=1.5 + 2.25)
sax_note7 = pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 2.25, end=1.5 + 2.625)
sax.notes.extend([sax_note1, sax_note2, sax_note3, sax_note4, sax_note5, sax_note6, sax_note7])

# Bass: Walking line in D (D2, F#2, G2, A2), with chromatic approaches
bass_note1 = pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.5 + 0.375)
bass_note2 = pretty_midi.Note(velocity=80, pitch=40, start=1.5 + 0.375, end=1.5 + 0.75)
bass_note3 = pretty_midi.Note(velocity=80, pitch=43, start=1.5 + 0.75, end=1.5 + 1.125)
bass_note4 = pretty_midi.Note(velocity=80, pitch=45, start=1.5 + 1.125, end=1.5 + 1.5)
bass_note5 = pretty_midi.Note(velocity=80, pitch=43, start=1.5 + 1.5, end=1.5 + 1.875)
bass_note6 = pretty_midi.Note(velocity=80, pitch=40, start=1.5 + 1.875, end=1.5 + 2.25)
bass_note7 = pretty_midi.Note(velocity=80, pitch=38, start=1.5 + 2.25, end=1.5 + 2.625)
bass.notes.extend([bass_note1, bass_note2, bass_note3, bass_note4, bass_note5, bass_note6, bass_note7])

# Piano: Open voicings, different chords each bar
# Bar 2: Dmaj7 (D, F#, A, C#)
piano_note1 = pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.5 + 0.75)
piano_note2 = pretty_midi.Note(velocity=90, pitch=66, start=1.5, end=1.5 + 0.75)
piano_note3 = pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.5 + 0.75)
piano_note4 = pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.5 + 0.75)
piano.notes.extend([piano_note1, piano_note2, piano_note3, piano_note4])

# Bar 3: Bm7 (B, D, F#, A)
piano_note5 = pretty_midi.Note(velocity=90, pitch=69, start=1.5 + 0.75, end=1.5 + 1.5)
piano_note6 = pretty_midi.Note(velocity=90, pitch=62, start=1.5 + 0.75, end=1.5 + 1.5)
piano_note7 = pretty_midi.Note(velocity=90, pitch=66, start=1.5 + 0.75, end=1.5 + 1.5)
piano_note8 = pretty_midi.Note(velocity=90, pitch=69, start=1.5 + 0.75, end=1.5 + 1.5)
piano.notes.extend([piano_note5, piano_note6, piano_note7, piano_note8])

# Bar 4: G7 (G, B, D, F)
piano_note9 = pretty_midi.Note(velocity=90, pitch=67, start=1.5 + 1.5, end=1.5 + 2.25)
piano_note10 = pretty_midi.Note(velocity=90, pitch=69, start=1.5 + 1.5, end=1.5 + 2.25)
piano_note11 = pretty_midi.Note(velocity=90, pitch=62, start=1.5 + 1.5, end=1.5 + 2.25)
piano_note12 = pretty_midi.Note(velocity=90, pitch=65, start=1.5 + 1.5, end=1.5 + 2.25)
piano.notes.extend([piano_note9, piano_note10, piano_note11, piano_note12])

# Bar 3: Drums (1.5 - 3.0s)
for beat in [0, 1, 2, 3]:
    note = pretty_midi.Note(velocity=100, pitch=42, start=(beat * 0.375) + 1.5, end=(beat * 0.375) + 1.625)
    drums.notes.append(note)
for beat in [0, 2]:
    note = pretty_midi.Note(velocity=110, pitch=38, start=(beat * 0.375) + 1.5, end=(beat * 0.375) + 1.625)
    drums.notes.append(note)
for beat in [0, 1, 2, 3]:
    note = pretty_midi.Note(velocity=80, pitch=36, start=(beat * 0.375) + 1.5, end=(beat * 0.375) + 1.625)
    drums.notes.append(note)

# Bar 4: Drums (3.0 - 4.5s)
for beat in [0, 1, 2, 3]:
    note = pretty_midi.Note(velocity=100, pitch=42, start=(beat * 0.375) + 3.0, end=(beat * 0.375) + 3.125)
    drums.notes.append(note)
for beat in [0, 2]:
    note = pretty_midi.Note(velocity=110, pitch=38, start=(beat * 0.375) + 3.0, end=(beat * 0.375) + 3.125)
    drums.notes.append(note)
for beat in [0, 1, 2, 3]:
    note = pretty_midi.Note(velocity=80, pitch=36, start=(beat * 0.375) + 3.0, end=(beat * 0.375) + 3.125)
    drums.notes.append(note)

# Bar 4: Sax continues motif
sax_note8 = pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 2.625, end=1.5 + 3.0)
sax.notes.append(sax_note8)

# Bar 4: Bass continues walking line
bass_note8 = pretty_midi.Note(velocity=80, pitch=38, start=1.5 + 2.625, end=1.5 + 3.0)
bass.notes.append(bass_note8)

# Bar 4: Piano resolves on Dmaj7
piano_note13 = pretty_midi.Note(velocity=90, pitch=62, start=1.5 + 2.25, end=1.5 + 3.0)
piano_note14 = pretty_midi.Note(velocity=90, pitch=66, start=1.5 + 2.25, end=1.5 + 3.0)
piano_note15 = pretty_midi.Note(velocity=90, pitch=69, start=1.5 + 2.25, end=1.5 + 3.0)
piano_note16 = pretty_midi.Note(velocity=90, pitch=71, start=1.5 + 2.25, end=1.5 + 3.0)
piano.notes.extend([piano_note13, piano_note14, piano_note15, piano_note16])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
