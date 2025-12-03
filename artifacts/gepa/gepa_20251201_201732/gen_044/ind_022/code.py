
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in D, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root), F#2 (fifth), chromatic approach to G2
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # F#2
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.5),   # chromatic
    pretty_midi.Note(velocity=100, pitch=43, start=2.5, end=2.875), # G2

    # Bar 3: A2 (root), C#2 (fifth), chromatic approach to B2
    pretty_midi.Note(velocity=100, pitch=42, start=2.875, end=3.25), # A2
    pretty_midi.Note(velocity=100, pitch=45, start=3.25, end=3.625), # C#2
    pretty_midi.Note(velocity=80, pitch=44, start=3.625, end=3.90625), # chromatic
    pretty_midi.Note(velocity=100, pitch=47, start=3.90625, end=4.28125), # B2

    # Bar 4: D2 (root), F#2 (fifth), chromatic approach to G2
    pretty_midi.Note(velocity=100, pitch=38, start=4.28125, end=4.65625), # D2
    pretty_midi.Note(velocity=100, pitch=41, start=4.65625, end=5.03125), # F#2
    pretty_midi.Note(velocity=80, pitch=40, start=5.03125, end=5.3125),   # chromatic
    pretty_midi.Note(velocity=100, pitch=43, start=5.3125, end=5.6875), # G2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D F# A C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # A4
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875), # C#4
]

# Bar 3: Amaj7 (A C# E G#)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=2.875, end=3.25), # A4
    pretty_midi.Note(velocity=100, pitch=74, start=2.875, end=3.25), # C#4
    pretty_midi.Note(velocity=100, pitch=76, start=2.875, end=3.25), # E4
    pretty_midi.Note(velocity=100, pitch=79, start=2.875, end=3.25), # G#4
])

# Bar 4: Dmaj7 (D F# A C#) again with a chromatic resolution into G
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.28125, end=4.65625), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.28125, end=4.65625), # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=4.28125, end=4.65625), # A4
    pretty_midi.Note(velocity=100, pitch=74, start=4.28125, end=4.65625), # C#4
    pretty_midi.Note(velocity=100, pitch=69, start=4.65625, end=5.03125), # G4
])
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62) B4 (67) F#4 (67) G4 (69) - resolution on D4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75), # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0), # B4
]
# Leave it hanging
# Come back and finish it
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25), # F#4
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5), # G4
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75), # D4
])
for note in sax_notes:
    sax.notes.append(note)

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2: 1.5 - 3.0s
for i in range(2):
    start = 1.5 + i * 1.5
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375), # Kick on 1
        pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875), # Snare on 2
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.1875),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5),
    ]
    for note in drum_notes:
        drums.notes.append(note)

# Bar 3 (3.0 - 4.5s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5), # Kick on 3
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875), # Snare on 2
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0), # Snare on 4
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4 (4.5 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0), # Kick on 3
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375), # Snare on 2
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.375), # Snare on 4 (out of range)
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
