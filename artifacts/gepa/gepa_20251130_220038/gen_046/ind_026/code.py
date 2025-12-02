
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
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100), # Hihat on &1
    (1.0, 38, 100),  # Snare on 2
    (1.5, 36, 100),  # Kick on 3
    (1.75, 42, 100), # Hihat on &3
    (2.0, 38, 100),  # Snare on 4
    (2.25, 42, 100), # Hihat on &4
    (2.5, 42, 100),  # Hihat on 1
    (3.0, 36, 100),  # Kick on 2
    (3.25, 42, 100), # Hihat on &2
    (3.5, 38, 100),  # Snare on 3
    (4.0, 36, 100),  # Kick on 4
    (4.25, 42, 100), # Hihat on &4
    (4.5, 38, 100),  # Snare on 1
    (4.75, 42, 100), # Hihat on &1
    (5.0, 36, 100),  # Kick on 2
    (5.25, 42, 100), # Hihat on &2
    (5.5, 38, 100),  # Snare on 3
    (6.0, 36, 100)   # Kick on 4
]
for note in drum_notes:
    dr = pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    (1.5, 64, 100),  # D
    (1.75, 65, 100), # Eb
    (2.0, 67, 100),  # F
    (2.25, 69, 100), # G
    (2.5, 71, 100),  # A
    (2.75, 72, 100), # Bb
    (3.0, 74, 100),  # B
    (3.25, 76, 100), # C
    (3.5, 78, 100),  # D
    (3.75, 79, 100), # Eb
    (4.0, 81, 100),  # F
    (4.25, 83, 100), # G
    (4.5, 85, 100),  # A
    (4.75, 86, 100), # Bb
    (5.0, 88, 100),  # B
    (5.25, 90, 100), # C
    (5.5, 92, 100),  # D
    (5.75, 93, 100), # Eb
    (6.0, 95, 100)   # F
]
for note in bass_notes:
    bn = pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25)
    bass.notes.append(bn)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.75, 69, 100), # G7: G, B, D, F
    (1.75, 71, 100),
    (1.75, 74, 100),
    (1.75, 76, 100),
    (2.25, 71, 100), # A7: A, C#, E, G
    (2.25, 74, 100),
    (2.25, 76, 100),
    (2.25, 79, 100),
    (3.75, 74, 100), # Bb7: Bb, D, F, Ab
    (3.75, 76, 100),
    (3.75, 79, 100),
    (3.75, 82, 100),
    (4.25, 76, 100), # B7: B, D#, F#, A
    (4.25, 79, 100),
    (4.25, 82, 100),
    (4.25, 84, 100),
    (5.75, 76, 100), # C7: C, E, G, Bb
    (5.75, 79, 100),
    (5.75, 81, 100),
    (5.75, 83, 100)
]
for note in piano_notes:
    pn = pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25)
    piano.notes.append(pn)

# Sax: Melody - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 69, 100),  # G - start of motif
    (1.75, 67, 100), # F
    (2.0, 69, 100),  # G
    (2.25, 71, 100), # A
    (2.5, 69, 100),  # G
    (2.75, 67, 100), # F
    (3.0, 69, 100),  # G
    (3.25, 71, 100), # A
    (3.5, 74, 100),  # B
    (3.75, 71, 100), # A
    (4.0, 69, 100),  # G
    (4.25, 67, 100), # F
    (4.5, 69, 100),  # G
    (4.75, 71, 100), # A
    (5.0, 74, 100),  # B
    (5.25, 76, 100), # C
    (5.5, 74, 100),  # B
    (5.75, 71, 100), # A
    (6.0, 69, 100)   # G
]
for note in sax_notes:
    sn = pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25)
    sax.notes.append(sn)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
