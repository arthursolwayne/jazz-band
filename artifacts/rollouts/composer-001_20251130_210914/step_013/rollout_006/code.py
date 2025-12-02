
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
kick_times = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_times = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875, 5.625]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125, 1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125, 3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125, 4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]

for t in kick_times:
    note = pretty_midi.Note(velocity=80, pitch=36, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=90, pitch=38, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=60, pitch=42, start=t, end=t + 0.0625)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 45, 80),   # F3
    (1.75, 46, 80),  # Gb3
    (2.0, 48, 80),   # A3
    (2.25, 49, 80),  # Bb3
    (2.5, 50, 80),   # B3
    (2.75, 52, 80),  # D4
    (3.0, 53, 80),   # Eb4
    (3.25, 55, 80),  # F4
    (3.5, 56, 80),   # Gb4
    (3.75, 58, 80),  # A4
    (4.0, 59, 80),   # Bb4
    (4.25, 60, 80),  # B4
    (4.5, 62, 80),   # D5
    (4.75, 63, 80),  # Eb5
    (5.0, 65, 80),   # F5
    (5.25, 66, 80),  # Gb5
    (5.5, 68, 80),   # A5
    (5.75, 69, 80),  # Bb5
]

for t, p, v in bass_notes:
    note = pretty_midi.Note(velocity=v, pitch=p, start=t, end=t + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (2.0, 50, 100),  # B3
    (2.0, 57, 100),  # G4
    (2.0, 60, 100),  # B4
    (2.0, 64, 100),  # D5
    (4.0, 50, 100),  # B3
    (4.0, 57, 100),  # G4
    (4.0, 60, 100),  # B4
    (4.0, 64, 100),  # D5
]

for t, p, v in piano_notes:
    note = pretty_midi.Note(velocity=v, pitch=p, start=t, end=t + 0.25)
    piano.notes.append(note)

# Sax: Short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 62, 110),  # D5
    (1.75, 65, 110), # F5
    (2.0, 67, 110),  # G5
    (2.25, 65, 110), # F5
    (2.5, 62, 110),  # D5
    (3.0, 69, 110),  # Bb5
    (3.25, 71, 110), # C6
    (3.5, 69, 110),  # Bb5
    (3.75, 67, 110), # G5
    (4.0, 65, 110),  # F5
    (4.25, 62, 110), # D5
    (4.5, 60, 110),  # B4
    (4.75, 58, 110), # A4
    (5.0, 55, 110),  # F4
    (5.25, 52, 110), # D4
    (5.5, 50, 110),  # B3
    (5.75, 48, 110), # A3
]

for t, p, v in sax_notes:
    note = pretty_midi.Note(velocity=v, pitch=p, start=t, end=t + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
