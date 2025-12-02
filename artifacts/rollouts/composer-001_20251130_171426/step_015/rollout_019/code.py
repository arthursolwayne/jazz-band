
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
bar_length = 1.5  # seconds
for beat in [0, 2]:  # 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=beat * 0.375, end=beat * 0.375 + 0.1))
for beat in [1, 3]:  # 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=beat * 0.375, end=beat * 0.375 + 0.1))
for beat in range(4):  # every eighth note
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=beat * 0.375, end=beat * 0.375 + 0.05))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, no repeating notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.5 + 0.375),  # D (root)
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=1.875 + 0.375),  # Eb (chromatic)
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.25 + 0.375),  # G (3rd)
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=2.625 + 0.375),  # A (5th)
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=2.625 + 0.375),  # G (3rd)
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.0 + 0.375),  # Eb (chromatic)
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.375 + 0.375),  # D (root)
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=3.75 + 0.375),  # C (chromatic)
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.125 + 0.375),  # D (root)
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.5 + 0.375),  # Eb (chromatic)
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=4.875 + 0.375),  # G (3rd)
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.25 + 0.375),  # A (5th)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Dm7 = D F A C
# Bar 2: comp on beat 2 (1.875)
piano.notes.append(pretty_midi.Note(velocity=85, pitch=50, start=1.875, end=1.875 + 0.1))  # F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=52, start=1.875, end=1.875 + 0.1))  # A
piano.notes.append(pretty_midi.Note(velocity=85, pitch=55, start=1.875, end=1.875 + 0.1))  # C
# Bar 3: comp on beat 2 (3.0)
piano.notes.append(pretty_midi.Note(velocity=85, pitch=50, start=3.0, end=3.0 + 0.1))  # F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=52, start=3.0, end=3.0 + 0.1))  # A
piano.notes.append(pretty_midi.Note(velocity=85, pitch=55, start=3.0, end=3.0 + 0.1))  # C
# Bar 4: comp on beat 2 (4.5)
piano.notes.append(pretty_midi.Note(velocity=85, pitch=50, start=4.5, end=4.5 + 0.1))  # F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=52, start=4.5, end=4.5 + 0.1))  # A
piano.notes.append(pretty_midi.Note(velocity=85, pitch=55, start=4.5, end=4.5 + 0.1))  # C

# Sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), F (65), A (67), G (67) -> D (62)
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.375),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=1.875 + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.25 + 0.375),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.625 + 0.375),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.5 + 0.375),  # D (finish motif)
]
sax.notes.extend(sax_notes)

# Drums continue in bars 2-4
for bar in range(2, 4):
    start = bar * bar_length
    for beat in [0, 2]:  # 1 and 3
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1))
    for beat in [1, 3]:  # 2 and 4
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1))
    for beat in range(4):  # every eighth note
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start + beat * 0.375, end=start + beat * 0.375 + 0.05))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
