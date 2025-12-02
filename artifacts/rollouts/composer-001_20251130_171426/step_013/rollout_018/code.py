
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
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375)   # Hihat on 4
]
for note_number, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in Fm, chromatic approaches
bass_notes = [
    (39, 1.5, 0.375),  # Fm root (F)
    (40, 1.875, 0.375),  # Gb (chromatic approach)
    (41, 2.25, 0.375),  # G (Fm 9)
    (43, 2.625, 0.375),  # A (Fm 11)
    (44, 2.625, 0.375),  # Bb (Fm 13)
    (42, 3.0, 0.375),  # Ab (chromatic approach)
    (38, 3.375, 0.375),  # F (root again)
    (40, 3.75, 0.375),  # Gb (approach)
    (41, 4.125, 0.375),  # G (Fm 9)
    (43, 4.5, 0.375),  # A (Fm 11)
    (44, 4.5, 0.375),  # Bb (Fm 13)
    (42, 4.875, 0.375),  # Ab (approach)
    (38, 5.25, 0.375),  # F (root again)
    (40, 5.625, 0.375),  # Gb (approach)
]
for note_number, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    bass.notes.append(note)

# Piano (Diane): 7th chords on 2 and 4, comping with tension
piano_notes = [
    # Bar 2: Fm7 on 2 and 4
    (39, 1.875, 0.375),  # F
    (43, 1.875, 0.375),  # A
    (42, 1.875, 0.375),  # Ab (b7)
    (46, 1.875, 0.375),  # C (7th)
    (39, 2.625, 0.375),  # F
    (43, 2.625, 0.375),  # A
    (42, 2.625, 0.375),  # Ab
    (46, 2.625, 0.375),  # C
    
    # Bar 3: Fm7 on 2 and 4 (same as bar 2)
    (39, 3.375, 0.375),
    (43, 3.375, 0.375),
    (42, 3.375, 0.375),
    (46, 3.375, 0.375),
    (39, 4.125, 0.375),
    (43, 4.125, 0.375),
    (42, 4.125, 0.375),
    (46, 4.125, 0.375),
    
    # Bar 4: Fm7 on 2 and 4 (same as bar 2)
    (39, 4.875, 0.375),
    (43, 4.875, 0.375),
    (42, 4.875, 0.375),
    (46, 4.875, 0.375),
    (39, 5.625, 0.375),
    (43, 5.625, 0.375),
    (42, 5.625, 0.375),
    (46, 5.625, 0.375),
]
for note_number, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    piano.notes.append(note)

# Saxophone (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (41, 1.5, 0.375),  # G (Fm 9)
    (43, 1.875, 0.375),  # A (Fm 11)
    (42, 2.25, 0.375),  # Ab (b7)
    (39, 2.625, 0.375),  # F (root)
    (41, 3.0, 0.375),  # G (Fm 9)
    (43, 3.375, 0.375),  # A (Fm 11)
    (42, 3.75, 0.375),  # Ab (b7)
    (39, 4.125, 0.375),  # F (root)
    (41, 4.5, 0.375),  # G (Fm 9)
    (43, 4.875, 0.375),  # A (Fm 11)
    (42, 5.25, 0.375),  # Ab (b7)
    (39, 5.625, 0.375),  # F (root)
]
for note_number, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    sax.notes.append(note)

# Drums: Bar 2-4
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    # Kick on 1 and 3
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=start + beat * 0.375, end=start + beat * 0.375 + 0.375)
        drums.notes.append(note)
    # Snare on 2 and 4
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=start + beat * 0.375, end=start + beat * 0.375 + 0.375)
        drums.notes.append(note)
    # Hihat on every eighth
    for beat in range(4):
        note = pretty_midi.Note(velocity=100, pitch=42, start=start + beat * 0.375, end=start + beat * 0.375 + 0.375)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("f_minor_intro.mid")
