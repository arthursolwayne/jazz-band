
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
kick_notes = [36]
snare_notes = [38]
hihat_notes = [42]

for bar in range(1):
    # Kick on beat 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=bar*1.5, end=bar*1.5 + 0.375)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=bar*1.5 + 0.75, end=bar*1.5 + 1.125)
    drums.notes.append(kick)
    
    # Snare on beat 2 and 4
    snare = pretty_midi.Note(velocity=110, pitch=38, start=bar*1.5 + 0.375, end=bar*1.5 + 0.75)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=110, pitch=38, start=bar*1.5 + 1.125, end=bar*1.5 + 1.5)
    drums.notes.append(snare)
    
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=bar*1.5 + i*0.375, end=bar*1.5 + i*0.375 + 0.1875)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in F, roots and fifths with chromatic approaches
# Bar 2: F - G - E - D (chromatic approach to E)
# Bar 3: A - Bb - G - F (chromatic approach to G)
# Bar 4: C - D - Bb - A (chromatic approach to Bb)

bass_notes = [
    # Bar 2
    (1.5, 53), (1.875, 55), (2.25, 51), (2.625, 49),
    # Bar 3
    (3.0, 57), (3.375, 58), (3.75, 55), (4.125, 53),
    # Bar 4
    (4.5, 60), (4.875, 62), (5.25, 58), (5.625, 57)
]

for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
# Bar 3: Bbmaj7 (Bb, D, F, Ab)
# Bar 4: Dm7 (D, F, A, C)

# Bar 2
piano.add_note(78, 100, 1.5, 1.875)
piano.add_note(82, 100, 1.5, 1.875)
piano.add_note(84, 100, 1.5, 1.875)
piano.add_note(87, 100, 1.5, 1.875)

# Bar 3
piano.add_note(76, 100, 3.0, 3.375)
piano.add_note(80, 100, 3.0, 3.375)
piano.add_note(84, 100, 3.0, 3.375)
piano.add_note(88, 100, 3.0, 3.375)

# Bar 4
piano.add_note(74, 100, 4.5, 4.875)
piano.add_note(76, 100, 4.5, 4.875)
piano.add_note(79, 100, 4.5, 4.875)
piano.add_note(84, 100, 4.5, 4.875)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (78) - G (80) - E (83) - F (78) (Bar 2)
#      : A (81) - Bb (82) - D (83) - E (85) (Bar 3)
#      : F (78) - G (80) - E (83) - D (82) (Bar 4)
# Bar 2: Play first two notes, leave it hanging
# Bar 3: Play next two notes, leave it hanging
# Bar 4: Finish the motif

# Bar 2
sax.add_note(78, 110, 1.5, 1.75)
sax.add_note(80, 110, 1.75, 2.0)

# Bar 3
sax.add_note(81, 110, 3.0, 3.25)
sax.add_note(82, 110, 3.25, 3.5)

# Bar 4
sax.add_note(78, 110, 4.5, 4.75)
sax.add_note(80, 110, 4.75, 5.0)
sax.add_note(83, 110, 5.0, 5.25)
sax.add_note(82, 110, 5.25, 5.5)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
