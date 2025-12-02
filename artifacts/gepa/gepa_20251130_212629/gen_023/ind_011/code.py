
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
drum_notes = [
    (36, 0.0, 0.375),    # Kick on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.0, 0.1875),   # Hihat on 1
    (42, 0.1875, 0.1875),# Hihat on &
    (42, 0.375, 0.1875), # Hihat on 2
    (42, 0.5625, 0.1875),# Hihat on &
    (42, 0.75, 0.1875),  # Hihat on 3
    (42, 0.9375, 0.1875),# Hihat on &
    (42, 1.125, 0.1875), # Hihat on 4
    (36, 1.125, 0.375),  # Kick on 3
    (38, 1.5, 0.375),    # Snare on 4
]

for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2: sax plays a motif, piano comps, bass walks, drums continue

# SAX: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm7 = F, Ab, C, Eb
# Motif: F (1.5s) -> Ab (2.125s) -> C (2.625s) -> rest (3.0s)
sax_notes = [
    (79, 1.5, 0.375),    # F (C4)
    (76, 2.125, 0.375),  # Ab (Eb4)
    (72, 2.625, 0.375),  # C (G4)
]
for note, start, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

# BASS: Walking line, chromatic approaches, no repeated notes
# Fm7 -> Bb7 -> Eb7 -> Am7
# F (1.5s), Gb (1.875s), Ab (2.25s), Bb (2.625s), C (2.875s), Db (3.25s), Eb (3.625s), D (4.0s)
bass_notes = [
    (71, 1.5, 0.375),    # F (F3)
    (70, 1.875, 0.375),  # Gb (F#3)
    (69, 2.25, 0.375),   # Ab (G3)
    (67, 2.625, 0.375),  # Bb (A3)
    (68, 2.875, 0.375),  # C (Bb3)
    (66, 3.25, 0.375),   # Db (Bb3)
    (65, 3.625, 0.375),  # Eb (Ab3)
    (64, 4.0, 0.375),    # D (G3)
]
for note, start, duration in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(bass_note)

# PIANO: 7th chords on 2 and 4, comp on 2 and 4
# Bar 2: Fm7 on beat 2
# Bar 3: Bb7 on beat 2
# Bar 4: Eb7 on beat 2

# Fm7 (F, Ab, C, Eb)
# Bb7 (Bb, D, F, Ab)
# Eb7 (Eb, G, Bb, Db)

# Bar 2: Fm7 (on beat 2)
piano_notes = [
    (79, 2.0, 0.1875),  # F (C4)
    (76, 2.0, 0.1875),  # Ab (Eb4)
    (72, 2.0, 0.1875),  # C (G4)
    (71, 2.0, 0.1875),  # Eb (F4)
]

# Bar 3: Bb7 (on beat 2)
piano_notes.extend([
    (77, 3.0, 0.1875),  # Bb (A4)
    (74, 3.0, 0.1875),  # D (Bb4)
    (79, 3.0, 0.1875),  # F (C5)
    (76, 3.0, 0.1875),  # Ab (Eb5)
])

# Bar 4: Eb7 (on beat 2)
piano_notes.extend([
    (69, 4.0, 0.1875),  # Eb (G4)
    (72, 4.0, 0.1875),  # G (Bb4)
    (77, 4.0, 0.1875),  # Bb (A5)
    (70, 4.0, 0.1875),  # Db (F#5)
])

for note, start, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(piano_note)

# Drums continue in bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 2
drum_notes = [
    (36, 1.5, 0.375),    # Kick on 1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.5, 0.1875),   # Hihat on 1
    (42, 1.6875, 0.1875),# Hihat on &
    (42, 1.875, 0.1875), # Hihat on 2
    (42, 2.0625, 0.1875),# Hihat on &
    (42, 2.25, 0.1875),  # Hihat on 3
    (42, 2.4375, 0.1875),# Hihat on &
    (42, 2.625, 0.1875), # Hihat on 4
    (36, 2.625, 0.375),  # Kick on 3
    (38, 3.0, 0.375),    # Snare on 4
]

for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

# Bar 3
drum_notes = [
    (36, 3.0, 0.375),    # Kick on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.0, 0.1875),   # Hihat on 1
    (42, 3.1875, 0.1875),# Hihat on &
    (42, 3.375, 0.1875), # Hihat on 2
    (42, 3.5625, 0.1875),# Hihat on &
    (42, 3.75, 0.1875),  # Hihat on 3
    (42, 3.9375, 0.1875),# Hihat on &
    (42, 4.125, 0.1875), # Hihat on 4
    (36, 4.125, 0.375),  # Kick on 3
    (38, 4.5, 0.375),    # Snare on 4
]

for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

# Bar 4
drum_notes = [
    (36, 4.5, 0.375),    # Kick on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.5, 0.1875),   # Hihat on 1
    (42, 4.6875, 0.1875),# Hihat on &
    (42, 4.875, 0.1875), # Hihat on 2
    (42, 5.0625, 0.1875),# Hihat on &
    (42, 5.25, 0.1875),  # Hihat on 3
    (42, 5.4375, 0.1875),# Hihat on &
    (42, 5.625, 0.1875), # Hihat on 4
    (36, 5.625, 0.375),  # Kick on 3
    (38, 6.0, 0.375),    # Snare on 4
]

for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("fm_intro.mid")
