
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25), # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.625), # C3
    pretty_midi.Note(velocity=90, pitch=59, start=2.625, end=3.0),  # D3

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=59, start=3.0, end=3.375),  # D3
    pretty_midi.Note(velocity=90, pitch=61, start=3.375, end=3.75), # E3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125), # F3
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),  # G3

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # G3
    pretty_midi.Note(velocity=90, pitch=66, start=4.875, end=5.25), # A3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625), # Bb3
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),  # C4
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875), # A4
    pretty_midi.Note(velocity=100, pitch=78, start=1.5, end=1.875), # C5
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=1.875), # E5

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375), # D5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375), # F5
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=3.375), # Ab5

    # Bar 4: E7 (E, G#, B, D)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875), # E5
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875), # G#5
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875), # B5
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.875), # D6
]
for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Melody in F: F - G - Bb - F (motif), but fragmented and left hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75), # F4
    pretty_midi.Note(velocity=110, pitch=72, start=1.75, end=2.0),  # G4
    pretty_midi.Note(velocity=110, pitch=76, start=2.0, end=2.25),  # Bb4
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.75), # F4 (sustained)
    pretty_midi.Note(velocity=110, pitch=71, start=2.75, end=3.0),  # F4 (release)
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25),  # F4 (start again)
    pretty_midi.Note(velocity=110, pitch=72, start=3.25, end=3.5),  # G4
    pretty_midi.Note(velocity=110, pitch=76, start=3.5, end=3.75),  # Bb4
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.25), # F4 (sustained)
    pretty_midi.Note(velocity=110, pitch=71, start=4.25, end=4.5),  # F4 (release)
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75),  # F4 (start again)
    pretty_midi.Note(velocity=110, pitch=72, start=4.75, end=5.0),  # G4
    pretty_midi.Note(velocity=110, pitch=76, start=5.0, end=5.25),  # Bb4
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=6.0),  # F4 (final sustain)
]
for note in sax_notes:
    sax.notes.append(note)

# Drums in bars 2-4
# Kick on 1 and 3
for bar in [1, 2, 3]:
    start = 1.5 + bar * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)

# Snare on 2 and 4
for bar in [1, 2, 3]:
    start = 1.5 + bar * 1.5
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)

# Hihat on every eighth
for bar in [1, 2, 3]:
    start = 1.5 + bar * 1.5
    for i in range(0, 4):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)

# Add the instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('jazz_intro.mid')
