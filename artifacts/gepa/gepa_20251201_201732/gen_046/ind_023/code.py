
import pretty_midi

# Create a new MIDI file with a tempo of 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers: kick=36, snare=38, hihat=42
drum_kick = 36
drum_snare = 38
drum_hihat = 42

# Bar duration in seconds at 160 BPM
bar_duration = 1.5  # 60 / 160 * 4 = 1.5s per bar
beat_duration = 0.375  # 60 / 160 = 0.375s per beat

# === BAR 1: DRUMS ONLY (0.0 - 1.5s) ===
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, drum_kick), (0.375, drum_hihat), (0.75, drum_snare),
    (1.125, drum_hihat), (1.5, drum_kick), (1.875, drum_hihat),
    (2.25, drum_snare), (2.625, drum_hihat)
]

for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# === BAR 2: FULL QUARTET (1.5 - 3.0s) ===

# BASS LINE (Marcus): D2 to G2, walking line with chromatic approaches
bass_notes = [
    (1.5, 38),  # D2
    (1.875, 40),  # Eb2 (chromatic approach)
    (2.25, 43),  # G2
    (2.625, 42),  # F#2 (chromatic approach)
]

for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# PIANO (Diane): Open voicings, different chord each bar
# Bar 2: D7 (no 9, open voicing)
piano_notes = [
    (1.5, 55),  # D4
    (1.5, 62),  # G4
    (1.5, 67),  # C5
    (1.5, 72),  # F5
    (2.25, 64),  # A4
    (2.25, 71),  # D5
    (2.25, 76),  # G5
    (2.25, 81),  # B5
]

for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# SAX (Dante): Short motif — D4, F4, G4, F4 — leave it hanging
sax_notes = [
    (1.5, 62),  # D4
    (1.875, 65),  # F4
    (2.25, 67),  # G4
    (2.625, 65),  # F4
]

for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(sax_note)

# === BAR 3: FULL QUARTET (3.0 - 4.5s) ===

# BASS LINE (Marcus): D2 to G2, walking line with chromatic approaches
bass_notes = [
    (3.0, 43),  # G2
    (3.375, 42),  # F#2
    (3.75, 38),  # D2
    (4.125, 40),  # Eb2
]

for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# PIANO (Diane): Different chord — Dmaj7 (open voicing)
piano_notes = [
    (3.0, 55),  # D4
    (3.0, 62),  # G4
    (3.0, 67),  # C5
    (3.0, 72),  # F5
    (3.75, 64),  # A4
    (3.75, 71),  # D5
    (3.75, 76),  # G5
    (3.75, 81),  # B5
]

for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# SAX (Dante): Return with the motif, but finish it
sax_notes = [
    (3.0, 62),  # D4
    (3.375, 65),  # F4
    (3.75, 67),  # G4
    (4.125, 62),  # D4
]

for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(sax_note)

# === BAR 4: FULL QUARTET (4.5 - 6.0s) ===

# BASS LINE (Marcus): D2 to G2, walking line with chromatic approaches
bass_notes = [
    (4.5, 40),  # Eb2
    (4.875, 38),  # D2
    (5.25, 43),  # G2
    (5.625, 42),  # F#2
]

for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# PIANO (Diane): Different chord — D7 (open voicing)
piano_notes = [
    (4.5, 55),  # D4
    (4.5, 62),  # G4
    (4.5, 67),  # C5
    (4.5, 72),  # F5
    (5.25, 64),  # A4
    (5.25, 71),  # D5
    (5.25, 76),  # G5
    (5.25, 81),  # B5
]

for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# SAX (Dante): Repeat the motif — leave it hanging again
sax_notes = [
    (4.5, 62),  # D4
    (4.875, 65),  # F4
    (5.25, 67),  # G4
    (5.625, 65),  # F4
]

for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(sax_note)

# === Add all instruments to MIDI file ===
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
