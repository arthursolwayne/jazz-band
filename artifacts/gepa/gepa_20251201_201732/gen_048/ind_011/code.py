
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
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5)
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass Line: Marcus, walking line in Fm (F, Ab, D, C), with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # Eb2
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),  # F#2 (chromatic approach)

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.75), # Eb2
    pretty_midi.Note(velocity=80, pitch=44, start=3.75, end=4.125), # Gb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),  # F#2

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25), # Eb2
    pretty_midi.Note(velocity=80, pitch=45, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),  # F#2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane, open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (1.5 - 3.0s): Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),   # F4
    pretty_midi.Note(velocity=90, pitch=51, start=1.5, end=3.0),   # Ab4
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=3.0),   # C5
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=3.0),   # Eb4

    # Bar 3 (3.0 - 4.5s): Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=4.5),   # Bb4
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=4.5),   # D5
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=4.5),   # F4
    pretty_midi.Note(velocity=80, pitch=51, start=3.0, end=4.5),   # Ab4

    # Bar 4 (4.5 - 6.0s): Eb7 (Eb, G, Bb, Db)
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=6.0),   # Eb4
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=6.0),   # G4
    pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=6.0),   # Bb4
    pretty_midi.Note(velocity=80, pitch=47, start=4.5, end=6.0),   # Db4
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante, one short motif, start and end on the same note, leave it hanging
sax_notes = [
    # Bar 2 (1.5 - 3.0s): motif starts
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),   # B4
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),   # A4

    # Bar 3 (3.0 - 4.5s): rest for tension
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.0),     # B4 (rest)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),     # B4 (rest)

    # Bar 4 (4.5 - 6.0s): return, leave it unfinished
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),   # B4
    pretty_midi.Note(velocity=110, pitch=60, start=4.875, end=5.25),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # B4
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),   # A4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4 (1.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 1.5)

drums_notes = []
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    dr = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    dr2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    sn = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    sn2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hi = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 1.5)
    drums_notes.append(dr)
    drums_notes.append(dr2)
    drums_notes.append(sn)
    drums_notes.append(sn2)
    drums_notes.append(hi)

for note in drums_notes:
    drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
