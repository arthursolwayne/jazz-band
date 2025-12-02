
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),   # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full Quartet (1.5 - 3.0s)
# Bass: F2 (38) to G2 (43) walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # F#2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),  # G#2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chords each bar, resolve on last beat
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.75),  # C5
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.75),  # E5
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.25),  # C5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.25),  # Eb5
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.25),  # G5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.25),  # Bb5
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Am7 (A, C, E, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.75),  # A5
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.75),  # C5
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=4.75),  # E5
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.75),  # G5
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif
# F4 -> G4 -> F4 (hanging)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=79, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=110, pitch=77, start=3.0, end=3.375),   # F4
    pretty_midi.Note(velocity=110, pitch=77, start=4.5, end=4.875),   # F4 (ending)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat every 8th
for bar in range(2, 5):  # Bars 2, 3, 4
    bar_start = bar * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.25)
    hihat_eighths = [bar_start + i * 0.375 for i in range(4)]
    for h in hihat_eighths:
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=h, end=bar_start + 1.5)
        drums.notes.append(hihat)
    drums.notes.append(kick1)
    drums.notes.append(snare2)
    drums.notes.append(kick3)
    drums.notes.append(snare4)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
