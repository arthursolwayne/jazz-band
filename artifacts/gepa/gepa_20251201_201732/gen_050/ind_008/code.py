
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36),   # Kick on beat 1
    (0.375, 42), # Hihat on 1&
    (0.75, 38),  # Snare on beat 2
    (1.125, 42), # Hihat on 2&
    (1.5, 36),   # Kick on beat 3
    (1.875, 42), # Hihat on 3&
    (2.25, 38),  # Snare on beat 4
    (2.625, 42)  # Hihat on 4&
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36),   # Kick on beat 1
    (1.875, 42), # Hihat on 1&
    (2.25, 38),  # Snare on beat 2
    (2.625, 42), # Hihat on 2&
    (3.0, 36),   # Kick on beat 3
    (3.375, 42), # Hihat on 3&
    (3.75, 38),  # Snare on beat 4
    (4.125, 42)  # Hihat on 4&
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: walking line with chromatic approaches, D2-G2 (MIDI 38-43)
bass_notes = [
    (1.5, 43),  # D2
    (1.75, 42), # Chromatic approach
    (2.0, 38),  # G2
    (2.25, 39), # Chromatic approach
    (2.5, 40),  # Chromatic approach
    (2.75, 38), # G2
    (3.0, 43),  # D2
    (3.25, 42), # Chromatic approach
    (3.5, 38),  # G2
    (3.75, 39), # Chromatic approach
    (4.0, 40),  # Chromatic approach
    (4.25, 38)  # G2
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: open voicings, resolve on last beat
# Bar 2: Dmaj7 (D, F#, A, C#)
piano_notes = [
    (1.5, 62),  # D4
    (1.5, 67),  # F#4
    (1.5, 74),  # A4
    (1.5, 71),  # C#4
    # Bar 3: G7 (G, B, D, F)
    (2.25, 67), # G4
    (2.25, 71), # B4
    (2.25, 62), # D4
    (2.25, 69), # F4
    # Bar 4: C#m7 (C#, E, G, B)
    (3.0, 69),  # C#4
    (3.0, 64),  # E4
    (3.0, 62),  # G4
    (3.0, 71),  # B4
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.75))

# Sax: one short motif, make it sing
# Start on D4 (62), play a melodic turn with 8th notes, leave it hanging
sax_notes = [
    (1.5, 62),  # D4
    (1.625, 64), # E4
    (1.75, 62),  # D4
    (1.875, 65), # F4
    (2.0, 62),   # D4
    (2.125, 64), # E4
    (2.25, 67),  # F#4 (leaving it hanging)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
