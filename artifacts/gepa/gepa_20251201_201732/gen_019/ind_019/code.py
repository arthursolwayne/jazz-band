
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
for i in range(4):
    note = pretty_midi.Note(velocity=100, pitch=36, start=i*0.375, end=i*0.375 + 0.375)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=(i+1)*0.375, end=(i+1)*0.375 + 0.375)
    drums.notes.append(note)
    for j in range(2):
        note = pretty_midi.Note(velocity=80, pitch=42, start=(i*2 + j)*0.1875, end=(i*2 + j)*0.1875 + 0.1875)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: F (38)
note = pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.5 + 0.375)
bass.notes.append(note)
# Bar 2: C (43)
note = pretty_midi.Note(velocity=100, pitch=43, start=1.5 + 0.75, end=1.5 + 0.75 + 0.375)
bass.notes.append(note)
# Bar 3: Bb (41) chromatic approach
note = pretty_midi.Note(velocity=100, pitch=41, start=1.5 + 1.5, end=1.5 + 1.5 + 0.375)
bass.notes.append(note)
# Bar 3: F (38)
note = pretty_midi.Note(velocity=100, pitch=38, start=1.5 + 1.5 + 0.75, end=1.5 + 1.5 + 0.75 + 0.375)
bass.notes.append(note)
# Bar 4: G (43)
note = pretty_midi.Note(velocity=100, pitch=43, start=1.5 + 3.0, end=1.5 + 3.0 + 0.375)
bass.notes.append(note)
# Bar 4: C (46)
note = pretty_midi.Note(velocity=100, pitch=46, start=1.5 + 3.0 + 0.75, end=1.5 + 3.0 + 0.75 + 0.375)
bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
note = pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.5 + 0.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.5 + 0.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.5 + 0.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.5 + 0.75)
piano.notes.append(note)

# Bar 3: Bb7 (Bb, D, F, Ab)
note = pretty_midi.Note(velocity=100, pitch=50, start=1.5 + 1.5, end=1.5 + 1.5 + 0.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=55, start=1.5 + 1.5, end=1.5 + 1.5 + 0.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=58, start=1.5 + 1.5, end=1.5 + 1.5 + 0.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=61, start=1.5 + 1.5, end=1.5 + 1.5 + 0.75)
piano.notes.append(note)

# Bar 4: C7 (C, E, G, B)
note = pretty_midi.Note(velocity=100, pitch=60, start=1.5 + 3.0, end=1.5 + 3.0 + 0.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 3.0, end=1.5 + 3.0 + 0.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 3.0, end=1.5 + 3.0 + 0.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 3.0, end=1.5 + 3.0 + 0.75)
piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, F (MIDI 60, 64, 62, 60)
note = pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.5 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 0.375, end=1.5 + 0.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 0.75, end=1.5 + 1.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=60, start=1.5 + 2.25, end=1.5 + 2.625)
sax.notes.append(note)

# Drums: Continue for bars 2-4
for i in range(6):
    if i < 4:
        start = 1.5 + i*0.375
    else:
        start = 1.5 + i*0.375 - 0.375
    note = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.375 + 0.375)
    drums.notes.append(note)
    for j in range(2):
        note = pretty_midi.Note(velocity=80, pitch=42, start=(start + j*0.1875), end=(start + j*0.1875) + 0.1875)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('wayne_intro.mid')
