
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
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with roots and fifths, chromatic approach
# Dm7 chord: D F A C
bass_notes = [
    # Bar 2
    (1.5, 38),  # D2
    (1.875, 41),  # F2 (chromatic approach to G2)
    (2.25, 43),  # G2
    (2.625, 38),  # D2
    # Bar 3
    (3.0, 40),  # A2
    (3.375, 38),  # D2 (chromatic approach to C2)
    (3.75, 40),  # A2
    (4.125, 38),  # D2
    # Bar 4
    (4.5, 38),  # D2
    (4.875, 41),  # F2 (chromatic approach to G2)
    (5.25, 43),  # G2
    (5.625, 38),  # D2
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D F A C)
    (1.5, 62),  # D4
    (1.5, 65),  # F4
    (1.5, 69),  # A4
    (1.5, 72),  # C5
    # Bar 3: G7 (G B D F)
    (3.0, 67),  # G4
    (3.0, 71),  # B4
    (3.0, 69),  # D4
    (3.0, 65),  # F4
    # Bar 4: Cm7 (C Eb G Bb)
    (4.5, 60),  # C4
    (4.5, 63),  # Eb4
    (4.5, 67),  # G4
    (4.5, 62),  # Bb4
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.5)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    (1.5, 62),  # D4
    (1.75, 65),  # F4
    (1.875, 62),  # D4
    # Bar 3
    (3.0, 65),  # F4
    (3.25, 67),  # G4
    (3.5, 65),  # F4
    # Bar 4
    (4.5, 62),  # D4
    (4.75, 65),  # F4
    (5.0, 67),  # G4
    (5.25, 65),  # F4
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Drums: continue the pattern for bars 2-4
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
