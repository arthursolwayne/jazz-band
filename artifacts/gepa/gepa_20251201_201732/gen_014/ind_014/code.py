
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
for beat in range(4):
    time = beat * 0.375
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.375 + 0.125)
    drums.notes.append(note)
    for eighth in range(2):
        note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
        drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Fm (F, Ab, G, Eb) with chromatic approaches
# F (F2), Ab (Ab2), G (G2), Eb (Eb2)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=37, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=1.875 + 0.375),
    pretty_midi.Note(velocity=90, pitch=39, start=2.25, end=2.25 + 0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=2.625, end=2.625 + 0.375)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=37, start=1.5, end=1.5 + 0.5),
    pretty_midi.Note(velocity=100, pitch=40, start=1.5, end=1.5 + 0.5),
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.5 + 0.5),
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.5 + 0.5)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F (F4), Ab (Ab4), G (G4), F (F4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.5 + 0.1875),
    pretty_midi.Note(velocity=110, pitch=69, start=1.6875, end=1.6875 + 0.1875),
    pretty_midi.Note(velocity=110, pitch=68, start=1.875, end=1.875 + 0.1875),
    pretty_midi.Note(velocity=110, pitch=67, start=2.0625, end=2.0625 + 0.1875)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in Fm (F, Ab, G, Eb)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=37, start=3.0, end=3.0 + 0.375),
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.375 + 0.375),
    pretty_midi.Note(velocity=90, pitch=39, start=3.75, end=3.75 + 0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=4.125, end=4.125 + 0.375)
]
bass.notes.extend(bass_notes)

# Piano: Bbm7 (Bb, Db, F, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.0 + 0.5),
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.0 + 0.5),
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.0 + 0.5),
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.0 + 0.5)
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=68, start=3.0, end=3.0 + 0.1875),
    pretty_midi.Note(velocity=110, pitch=67, start=3.1875, end=3.1875 + 0.1875),
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.375 + 0.1875),
    pretty_midi.Note(velocity=110, pitch=67, start=3.5625, end=3.5625 + 0.1875)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in Fm (F, Ab, G, Eb)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=37, start=4.5, end=4.5 + 0.375),
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=4.875 + 0.375),
    pretty_midi.Note(velocity=90, pitch=39, start=5.25, end=5.25 + 0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=5.625, end=5.625 + 0.375)
]
bass.notes.extend(bass_notes)

# Piano: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=37, start=4.5, end=4.5 + 0.5),
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.5 + 0.5),
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.5 + 0.5),
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.5 + 0.5)
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.5 + 0.1875),
    pretty_midi.Note(velocity=110, pitch=69, start=4.6875, end=4.6875 + 0.1875),
    pretty_midi.Note(velocity=110, pitch=68, start=4.875, end=4.875 + 0.1875),
    pretty_midi.Note(velocity=110, pitch=67, start=5.0625, end=5.0625 + 0.1875)
]
sax.notes.extend(sax_notes)

# Drums: continue pattern
for beat in range(4):
    time = (beat + 4) * 0.375
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.375 + 0.125)
    drums.notes.append(note)
    for eighth in range(2):
        note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
