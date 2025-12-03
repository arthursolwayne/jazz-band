
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),   # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),   # Hihat
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line (D2-G2), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0),  # A2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.75), # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.125), # D2
    pretty_midi.Note(velocity=80, pitch=40, start=4.125, end=4.5),  # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),  # G2
    pretty_midi.Note(velocity=80, pitch=45, start=4.875, end=5.25), # A2
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=80, pitch=41, start=5.625, end=6.0),  # F2
]

for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C E♭)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F (F4)
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # A (A4)
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=1.875),  # C (C5)
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),  # E♭ (E♭4)
    pretty_midi.Note(velocity=90, pitch=79, start=2.25, end=2.625), # C (C5)
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625), # A (A4)
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625), # F (F4)
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625), # E♭ (E♭4)
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=3.0),  # A (A4)
    pretty_midi.Note(velocity=90, pitch=79, start=2.625, end=3.0),  # C (C5)
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=3.0),  # E♭ (E♭4)
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),  # F (F4)
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.375),  # C (C5)
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # A (A4)
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # E♭ (E♭4)
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # F (F4)
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.125), # A (A4)
    pretty_midi.Note(velocity=90, pitch=79, start=3.75, end=4.125), # C (C5)
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.125), # E♭ (E♭4)
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125), # F (F4)
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.875),  # C (C5)
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # A (A4)
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),  # E♭ (E♭4)
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # F (F4)
    pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.625), # A (A4)
    pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.625), # C (C5)
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625), # E♭ (E♭4)
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625), # F (F4)
    pretty_midi.Note(velocity=90, pitch=79, start=5.625, end=6.0),  # C (C5)
    pretty_midi.Note(velocity=90, pitch=76, start=5.625, end=6.0),  # A (A4)
    pretty_midi.Note(velocity=90, pitch=74, start=5.625, end=6.0),  # E♭ (E♭4)
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),  # F (F4)
]

for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # B4
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.5),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # B4
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # B4
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25),  # B4
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # B4
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.5),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),  # B4
    pretty_midi.Note(velocity=100, pitch=66, start=5.75, end=6.0),  # G4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    snare = pretty_midi.Note(velocity=90, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    hihat_1 = pretty_midi.Note(velocity=90, pitch=42, start=bar_start, end=bar_start + 0.375)
    hihat_2 = pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75)
    hihat_3 = pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125)
    hihat_4 = pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5)
    drums.notes.append(kick)
    drums.notes.append(snare)
    drums.notes.append(hihat_1)
    drums.notes.append(hihat_2)
    drums.notes.append(hihat_3)
    drums.notes.append(hihat_4)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
