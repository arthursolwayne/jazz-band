
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
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

for i in range(2):
    kick_time = 0.0 + i * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.15)
    drums.notes.append(kick)

for i in range(2):
    snare_time = 0.375 + i * 1.5
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.15)
    drums.notes.append(snare)

for i in range(8):
    hihat_time = 0.0 + i * 0.375
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.1)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line in D, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.5 + 0.375),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.5 + 0.375, end=1.5 + 0.75),  # F#2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5 + 0.75, end=1.5 + 1.125),  # A2
    pretty_midi.Note(velocity=80, pitch=43, start=1.5 + 1.125, end=1.5 + 1.5),  # Bb2 (chromatic approach)

    pretty_midi.Note(velocity=80, pitch=43, start=1.5 + 1.5, end=1.5 + 1.875),  # Bb2
    pretty_midi.Note(velocity=80, pitch=38, start=1.5 + 1.875, end=1.5 + 2.25),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.5 + 2.25, end=1.5 + 2.625),  # F#2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5 + 2.625, end=1.5 + 3.0),  # A2

    pretty_midi.Note(velocity=80, pitch=42, start=1.5 + 3.0, end=1.5 + 3.375),  # A2
    pretty_midi.Note(velocity=80, pitch=43, start=1.5 + 3.375, end=1.5 + 3.75),  # Bb2
    pretty_midi.Note(velocity=80, pitch=38, start=1.5 + 3.75, end=1.5 + 4.125),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.5 + 4.125, end=1.5 + 4.5),  # F#2

    pretty_midi.Note(velocity=80, pitch=40, start=1.5 + 4.5, end=1.5 + 4.875),  # F#2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5 + 4.875, end=1.5 + 5.25),  # A2
    pretty_midi.Note(velocity=80, pitch=43, start=1.5 + 5.25, end=1.5 + 5.625),  # Bb2
    pretty_midi.Note(velocity=80, pitch=38, start=1.5 + 5.625, end=1.5 + 6.0),  # D2
]
bass.notes.extend(bass_notes)

# Diane on piano: open voicings, resolve on the last beat
# Bar 2: D7 (G, B, D, F#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + 0.375),  # G4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.5 + 0.375),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.5 + 0.375),  # D5
    pretty_midi.Note(velocity=100, pitch=80, start=1.5, end=1.5 + 0.375),  # F#5

    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 1.5, end=1.5 + 1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 1.5, end=1.5 + 1.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=74, start=1.5 + 1.5, end=1.5 + 1.875),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=1.5 + 1.5, end=1.5 + 1.875),  # F5

    # Bar 4: Cmaj7 (C, E, G, B)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 3.0, end=1.5 + 3.375),  # C4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5 + 3.0, end=1.5 + 3.375),  # E4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5 + 3.0, end=1.5 + 3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=81, start=1.5 + 3.0, end=1.5 + 3.375),  # B4

    # Resolutions on beat 4 (last beat of each bar)
    pretty_midi.Note(velocity=100, pitch=74, start=1.5 + 0.75, end=1.5 + 1.125),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=1.5 + 2.25, end=1.5 + 2.625),  # F5
    pretty_midi.Note(velocity=100, pitch=76, start=1.5 + 4.5, end=1.5 + 4.875),  # G4
]
piano.notes.extend(piano_notes)

# Dante on sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.5 + 0.375),  # B4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 0.75, end=1.5 + 1.125),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=1.5 + 1.5, end=1.5 + 1.875),  # E5
    pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 2.25, end=1.5 + 2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 3.0, end=1.5 + 3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 3.75, end=1.5 + 4.125),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=1.5 + 4.5, end=1.5 + 4.875),  # E5
    pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 5.25, end=1.5 + 5.625),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 5.625, end=1.5 + 6.0),  # B4
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(3):
    kick_time = 1.5 + i * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.15)
    drums.notes.append(kick)
    kick_time = 1.5 + i * 1.5 + 0.75
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.15)
    drums.notes.append(kick)

for i in range(3):
    snare_time = 1.5 + i * 1.5 + 0.375
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.15)
    drums.notes.append(snare)
    snare_time = 1.5 + i * 1.5 + 1.125
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.15)
    drums.notes.append(snare)

for i in range(12):
    hihat_time = 1.5 + i * 0.375
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.1)
    drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
