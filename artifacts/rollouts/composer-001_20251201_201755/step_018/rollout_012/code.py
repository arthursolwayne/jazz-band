
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25), # Bb (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # C (root of Bb7)
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # Bb (fifth of F7)
    
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # C (root of F7)
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75), # D (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125), # E (root of C7)
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),  # D (fifth of Bb7)
    
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # E (root of C7)
    pretty_midi.Note(velocity=100, pitch=78, start=4.875, end=5.25), # F# (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=81, start=5.25, end=5.625), # A (root of D7)
    pretty_midi.Note(velocity=100, pitch=78, start=5.625, end=6.0),  # F# (fifth of C7)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.25),  # E
]

# Bar 3: Bb7
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=3.0),  # Ab
]

# Bar 4: C7
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # Bb
]

# Add resolution on last bar
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.25),  # A (extension)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.25),  # C (root)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=5.25),  # E (third)
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=5.25),  # A (root of D7)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif in F, one short motif, make it sing
# First note on bar 2 (start=1.5), leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=110, pitch=76, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=110, pitch=76, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=110, pitch=72, start=5.625, end=6.0),  # C
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    for beat in [0, 2]:
        kick_start = bar_start + beat * 0.75
        kick_end = kick_start + 0.375
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    # Snare on 2 and 4
    for beat in [1, 3]:
        snare_start = bar_start + beat * 0.75
        snare_end = snare_start + 0.375
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
    # Hihat on every 8th
    for eighth in range(0, 4):
        hihat_start = bar_start + eighth * 0.375
        hihat_end = hihat_start + 0.375
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_end))

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
