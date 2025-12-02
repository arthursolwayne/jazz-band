
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
for beat in range(4):
    time = beat * 0.375
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeating notes
# Dm7: D F A C
# Start on F, walk down chromatically
bass_notes = [62, 61, 60, 59, 62, 61, 60, 59, 62, 61, 60, 59, 62, 61, 60, 59]
for i, pitch in enumerate(bass_notes):
    time = 1.5 + (i * 0.375)
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Dm7 = D F A C
# Comp on beats 2 and 4 of each bar
chord_notes = [50, 53, 57, 60]  # Dm7
for bar in range(3):
    for beat in range(4):
        time = 1.5 + (bar * 1.5) + (beat * 0.375)
        if beat % 2 == 1:
            for pitch in chord_notes:
                note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
                piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(3):
    for beat in range(4):
        time = 1.5 + (bar * 1.5) + (beat * 0.375)
        if beat % 2 == 0:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        else:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Sax: Motif in Dm. Start with a simple phrase that sings
# Dm scale: D Eb F G Ab Bb C
# Motif: D, Eb, F, G (4 notes)
sax_notes = [52, 53, 55, 57]
for i, pitch in enumerate(sax_notes):
    time = 1.5 + (i * 0.375)
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# End of motif, leave it hanging
# Repeat the first note, D, with a slight delay
note = pretty_midi.Note(velocity=110, pitch=52, start=3.0, end=3.25)
sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
