
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
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),  # kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),  # snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=36, start=0.75, end=1.125),  # kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),   # snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bass line in Fm (F, Ab, Bb, Db)
# Walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.25), # Eb (chromatic)
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=2.625, end=3.0),  # D (chromatic)

    # Bar 3
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=59, start=3.375, end=3.75), # C (chromatic)
    pretty_midi.Note(velocity=80, pitch=59, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=80, pitch=57, start=4.125, end=4.5),  # Bb (chromatic)

    # Bar 4
    pretty_midi.Note(velocity=80, pitch=57, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=55, start=4.875, end=5.25), # Ab (chromatic)
    pretty_midi.Note(velocity=80, pitch=55, start=5.25, end=5.625), # Ab
    pretty_midi.Note(velocity=80, pitch=53, start=5.625, end=6.0),  # G (chromatic)
]

for note in bass_notes:
    bass.notes.append(note)

# Diane - Piano comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),  # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.25),

    # Bar 3
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75),  # F7
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75),

    # Bar 4
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25),  # F7
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25),
]

for note in piano_notes:
    piano.notes.append(note)

# Dante - Tenor sax melody
# Start with a whisper, build to something urgent
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.625),  # D (quiet start)
    pretty_midi.Note(velocity=80, pitch=64, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.0),   # E (rest in between)

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.125),  # D (build)
    pretty_midi.Note(velocity=90, pitch=64, start=2.125, end=2.25), # F
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.375), # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.375, end=2.5),  # E

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.625), # F (urgent)
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=2.75), # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=2.875), # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.875, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.125, end=3.25), # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.625, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.875), # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.875, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.25), # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.375), # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.375, end=4.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.75), # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.0),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.125),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.125, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.375), # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.375, end=5.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=5.75), # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=5.875), # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.875, end=6.0),  # E
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=90, pitch=36, start=start, end=start + 0.375),
    # Snare on 2
    pretty_midi.Note(velocity=90, pitch=38, start=start + 0.375, end=start + 0.75),
    # Kick on 3
    pretty_midi.Note(velocity=90, pitch=36, start=start + 0.75, end=start + 1.125),
    # Snare on 4
    pretty_midi.Note(velocity=90, pitch=38, start=start + 1.125, end=start + 1.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
