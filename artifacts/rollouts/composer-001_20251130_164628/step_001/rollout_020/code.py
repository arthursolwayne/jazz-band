
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

# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.625, end=1.75), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=1.875), # C
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.125),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=2.125, end=2.25), # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.375), # C
    pretty_midi.Note(velocity=90, pitch=59, start=2.375, end=2.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=2.5, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=2.75), # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=2.875), # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.875, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.125),  # E
    pretty_midi.Note(velocity=90, pitch=59, start=3.125, end=3.25), # D
    pretty_midi.Note(velocity=90, pitch=57, start=3.25, end=3.375), # C
    pretty_midi.Note(velocity=90, pitch=59, start=3.375, end=3.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=3.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=3.625, end=3.75), # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=3.875), # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.875, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.0, end=4.125),  # E
    pretty_midi.Note(velocity=90, pitch=59, start=4.125, end=4.25), # D
    pretty_midi.Note(velocity=90, pitch=57, start=4.25, end=4.375), # C
    pretty_midi.Note(velocity=90, pitch=59, start=4.375, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=4.625, end=4.75), # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),   # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Dm7: D, F, A, C
# G7: G, B, D, F
# Cm7: C, Eb, G, Bb
# F7: F, A, C, Eb
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.625),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.625),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.0),  # B
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.375), # C
    pretty_midi.Note(velocity=90, pitch=63, start=2.25, end=2.375), # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.375), # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.375), # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=2.75), # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.75), # A
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.75), # C
    pretty_midi.Note(velocity=90, pitch=63, start=2.625, end=2.75), # Eb
]
piano.notes.extend(piano_notes)

# Sax: motif, short, singable, leave it hanging
# Dm - D, F, A, C
# Motif: D - F - A (half note, half note, quarter note)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=2.25),  # D (half note)
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=3.0),   # F (half note)
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # A (quarter note)
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=4.25), # D (quarter note, delayed)
]
sax.notes.extend(sax_notes)

# Drums: continue same pattern
for bar in range(2, 4):
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

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
